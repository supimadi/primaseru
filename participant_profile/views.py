import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, QueryDict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

from crispy_forms.utils import render_crispy_form

from . import models, forms
from .initial_forms import initial_forms
from dashboard.models import ParticipantGraduation, ParticipantLMS

@login_required
def index(request):

    if request.method == 'POST':
        try:
            photo = models.PhotoProfile.objects.get(participant=request.user.pk)
            form = forms.PhotoProfileForm(request.POST, request.FILES, instance=photo)
        except Exception:
            form = forms.PhotoProfileForm(request.POST, request.FILES)
            form.instance.participant = request.user

        if form.is_valid():
            form.save()
            return redirect('profile')

    try:
        kelulusan = ParticipantGraduation.objects.get(participant=request.user)
    except ParticipantGraduation.DoesNotExist:
        kelulusan = False

    return render(request, 'participant_profile/primaseru.html', {'kelulusan': kelulusan})

@login_required
def initial_photo(request):
    form = forms.PhotoProfileForm()
    if request.method == 'POST':
        try:
            photo = models.PhotoProfile.objects.get(participant=request.user.pk)
            form = forms.PhotoProfileForm(request.POST, request.FILES, instance=photo)
        except Exception:
            form = forms.PhotoProfileForm(request.POST, request.FILES)
            form.instance.participant = request.user

        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'participant_profile/initial_form_photo.html', {'form': form, 'step': 8})


class InitialFormView(LoginRequiredMixin, View):
    form_classes = [ # Pairing the form with it model
        [
            initial_forms.ParticipantProfileForm,
            models.ParticipantProfile,
        ],
        [
            initial_forms.ParticipantAddressForm,
            models.ParticipantProfile,
        ],
        [
            initial_forms.ParticipantMedicalRecord,
            models.ParticipantProfile,
        ],
        [
            initial_forms.ParticipantParentProfileForm,
            models.FatherStudentProfile,
        ],
        [
            initial_forms.ParticipantParentProfileForm,
            models.MotherStudentProfile,
        ],
        [
            initial_forms.ParticipantParentProfileForm,
            models.StudentGuardianProfile,
        ],
        [
            initial_forms.MajorParticipantForm,
            models.MajorStudent,
        ],
    ]
    template_name = 'participant_profile/initial_form.html'

    def get(self, request, *args, **kwargs):
        # Retrive or set a value to session
        try:
            step = request.session['step']
        except KeyError:
            step = request.session['step'] = 1

        data = request.session.get(f'{step}_data')
        model = self.form_classes[step-1][1].__name__

        # If user click previous retrive
        # data from session
        try:
           if not 'previous' in data:
               initial = data
           else:
               initial = {'step': step, 'model': model}
        except Exception:
               initial = {'step': step, 'model': model}

        form =  self.form_classes[step-1][0](initial=initial)
        return render(request, self.template_name, {'form': form, 'step': step})

    def _save_to_db(self, request):
        """
        Save form data from session to database
        """
        data = None
        for model in self.form_classes:
            # check if the data is the same as before
            if data == request.session[f'{model[1].__name__}_data']:
                continue
            data = request.session[f'{model[1].__name__}_data']

            # Delete unnecessary keys and values
            try:
                del data['step']
                del data['model']
                del data['csrfmiddlewaretoken']
                data['date_born'] = datetime.datetime.strptime(data['date_born'], '%d/%m/%Y').strftime('%Y-%m-%d')
            except KeyError:
                pass
            # change date format and then save it to db
            # data_model = model[1].objects.create(**data, participant_id=request.user.pk)
            # data_model.save()

    def _previous_form(self, request):
        """
        Just decrement step from session
        """
        step = request.session['step']

        if step == 1:
            return
        else:
            request.session["step"] -= 1

    def post(self, request, *args, **kwargs):
        step = request.session['step']
        if request.POST.get('step'):
            request.session[f'{step}_data'] = request.POST.dict()

        request.session['model'] = request.POST.get('model', None)
        form =  self.form_classes[step-1][0](request.POST)

        if request.POST.get('previous') == 'previous':
            self._previous_form(request)
            return redirect('initial-form')

        if not form.is_valid():
            return render(request, self.template_name, {'form': form, 'step': step})

        # create session for form data, or append to it when
        # the model name are the same
        try:
            request.session[f'{request.POST["model"]}_data'].update(request.POST.dict())
        except Exception:
            request.session[f'{request.POST["model"]}_data'] = request.POST.dict()

        # Check if step already max, save the form data to db
        if request.session['step'] == len(self.form_classes):
            self._save_to_db(request)
            return redirect('initial-photo')

        request.session['step'] += 1
        return redirect('initial-form')


class ProfileView(LoginRequiredMixin, View):
    """
    Create base view for creating and updating
    StudentProfile, FatherProfile, MotherProfile,
    and GuardianProfile. This class gonna be the basis
    for other class.
    """
    form_class = forms.ParticipantProfileForm
    model = models.ParticipantProfile
    template_name = 'participant_profile/profile.html'
    name = 'peserta'

    def get(self, request, *args, **kwargs):

        # make sure the request came from ajax
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            raise PermissionDenied

        try:
            data = self.model.objects.get(participant=request.user)
            form = self.form_class(instance=data)
        except self.model.DoesNotExist:
            data = None
            form = self.form_class()

        return render(request, self.template_name, {"form": form, "name": self.name, "data": data})

    def post(self, request, *args, **kwargs):

        try:
            data = self.model.objects.get(participant=request.user)
            if data.verified: # when data is validated user cannot edit it
                return JsonResponse({'success': False}, status=403)

            form = self.form_class(request.POST, request.FILES or None, instance=data)

        except (self.model.DoesNotExist, ValueError):
            form = self.form_class(request.POST, request.FILES or None)

        ctx = {}
        ctx.update(csrf(request))

        if form.is_valid():
            form.save(commit=False)
            form.instance.participant = request.user

            form.save(commit=True)
            form = render_crispy_form(form, context=ctx)
            return JsonResponse({'success': True, 'form_s': form}, status=200)

        form = render_crispy_form(form, context=ctx)
        return JsonResponse({'success': False, 'form_s': form}, status=400)

class FatherProfileView(ProfileView):
    form_class = forms.FatherParticipantForm
    model = models.FatherStudentProfile
    name = "ayah"

class MotherProfileView(ProfileView):
    form_class = forms.MotherParticipantForm
    model = models.MotherStudentProfile
    name = "ibu"

class GuardianProfileView(ProfileView):
    form_class = forms.GuardianParticipantForm
    model = models.StudentGuardianProfile
    name = "wali"

class MajorParticipantView(ProfileView):
    form_class = forms.ParticipantMajorForm
    model = models.MajorStudent
    name = "jurusan"

class ParticipantFilesView(ProfileView):
    form_class = forms.ParticipantFilesForm
    model = models.StudentFile
    template_name = "participant_profile/participant_files.html"
    name = "berkas"

class ParticipantLMSAccount(LoginRequiredMixin, View):
    model = ParticipantLMS
    template_name = "participant_profile/lms_account.html"

    def get(self, request, *args, **kwargs):
        try:
            data = self.model.objects.get(participant=request.user)
        except self.model.DoesNotExist:
            data = None

        return render(request, self.template_name, {'data': data})

class ParticipantGraduationView(ParticipantLMSAccount):
    model = ParticipantGraduation
    template_name = "participant_profile/graduation.html"

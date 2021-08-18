import datetime

from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, QueryDict
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

from crispy_forms.utils import render_crispy_form

from . import models, forms
from .mixins import IsPassessTestPPDB
from .initial_forms import initial_forms
from dashboard.models import ParticipantGraduation, ParticipantLMS, Participant, ParticipantRePayment

@login_required
def index(request):
    if request.user.is_staff:
        return redirect('dashboard')

    participant = Participant.objects.get(account=request.user.pk)
    if not participant.verified:
        return render(request, 'participant_profile/payment.html')

    return redirect('participant-major')

@login_required
def set_photo_profile(request):
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

        return redirect('profile')

    form = forms.PhotoProfileForm()
    return render(request, 'participant_profile/set_photo_profile.html', {'form': form})

@login_required
def id_card(request):
    data = models.ParticipantProfile.objects.get(participant=request.user.pk)
    image = models.PhotoProfile.objects.get(participant=request.user.pk)

    return render(request, 'participant_profile/id_card.html', {'data': data, 'image': image})

@login_required
def upload_files(request):
    try:
        data = models.StudentFile.objects.get(participant=request.user.pk)
    except models.StudentFile.DoesNotExist:
        data = None

    form = forms.ParticipantFilesForm(instance=data)
    if request.method == 'POST':
        form = forms.ParticipantFilesForm(request.POST, request.FILES, instance=data)

        if form.is_valid():
            form.save()
            messages.success(request, f'Berkas berhasil di upload.')
            return redirect('files-upload')

    return render(request, 'participant_profile/upload_files.html', {'form': form, 'data': data})


class ProfileView(LoginRequiredMixin, View):
    """
    Create base view for creating and updating
    StudentProfile, FatherProfile, MotherProfile,
    and GuardianProfile. This class gonna be the basis
    for other class.
    """
    form_class = forms.ParticipantProfileForm
    model = models.ParticipantProfile
    template_name = 'participant_profile/primaseru.html'
    url_name =  'participant-profile'
    name = 'peserta'

    def _get_context(self, data, form):
        try:
            pass_test = ParticipantGraduation.objects.get(participant=self.request.user.pk).passed
        except ParticipantGraduation.DoesNotExist:
            pass_test = None

        return {
            'form_ph': forms.PhotoProfileForm(),
            'form': form,
            'name': self.name,
            'data': data,
            'pass_test': pass_test
        }

    def get(self, request, *args, **kwargs):
        request.session['button'] = request.headers.get('X-Button-Clicked')

        try:
            data = self.model.objects.get(participant=request.user)
            form = self.form_class(instance=data)
        except self.model.DoesNotExist:
            data = None
            form = self.form_class()

        return render(request, self.template_name, self._get_context(data, form))

    def post(self, request, *args, **kwargs):

        try:
            data = self.model.objects.get(participant=request.user)
            # if data.verified: # when data is validated user cannot edit it
            #     return JsonResponse({'success': False}, status=403)

            form = self.form_class(request.POST, request.FILES or None, instance=data)

        except (self.model.DoesNotExist, ValueError):
            form = self.form_class(request.POST, request.FILES or None)

        if form.is_valid():
            form.save(commit=False)
            form.instance.participant = request.user

            form.save(commit=True)
            messages.success(request, f'Data {self.name} berhasil di upload.')
            return redirect(self.url_name)

        return render(request, self.template_name, self._get_context(data, form))

class ParticipantProfileView(IsPassessTestPPDB, ProfileView):
    form_class = forms.ParticipantProfileForm
    model = models.ParticipantProfile
    template_name = 'participant_profile/primaseru.html'
    url_name =  'participant-profile'
    name = 'peserta'

class FatherProfileView(IsPassessTestPPDB, ProfileView):
    form_class = forms.FatherParticipantForm
    model = models.FatherStudentProfile
    url_name = 'participant-father'
    name = "ayah"

class MotherProfileView(IsPassessTestPPDB, ProfileView):
    form_class = forms.MotherParticipantForm
    model = models.MotherStudentProfile
    url_name = 'participant-mother'
    name = "ibu"

class GuardianProfileView(IsPassessTestPPDB, ProfileView):
    form_class = forms.GuardianParticipantForm
    model = models.StudentGuardianProfile
    url_name = 'participant-guardian'
    name = "wali"

class MajorParticipantView(ProfileView):
    form_class = forms.ParticipantMajorForm
    model = models.MajorStudent
    url_name = 'participant-major'
    name = "jurusan"

class ParticipantKKView(ProfileView):
    form_class = forms.ParticipantKKForm
    model = models.StudentFile
    url_name = 'participant-kk'
    # template_name = "participant_profile/participant_files.html"
    name = "Kartu Keluarga"

class ParticipantLMSAccount(ProfileView):
    model = ParticipantLMS
    url_name = 'participant-lms'
    template_name = "participant_profile/lms_account.html"
    name = "LMS"

class ParticipantGraduationView(ProfileView):
    model = ParticipantGraduation
    url_name = 'participant-graduation'
    template_name = "participant_profile/graduation.html"
    name = 'graduation'

class RePaymentPage(IsPassessTestPPDB, ProfileView):
    model = ParticipantRePayment
    form_class = forms.ParticipantRePaymentForm
    url_name = 'participant-payment'
    template_name = "participant_profile/re_payment.html"
    name = 'Pembayaran Daftar Ulang'

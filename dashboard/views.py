from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import permission_required
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.core.exceptions import FieldError, ObjectDoesNotExist

from users.models import CustomUser
from users.mixins import UserIsStaffMixin

from . import forms

from .models import ParticipantCount, RegisterSchedule, RegisterStep, Participant
from .generator import register_number_generator

from participant_profile.models import (
    ParticipantProfile, MotherStudentProfile,
    FatherStudentProfile, StudentGuardianProfile,
    StudentFile, MajorStudent
)
from participant_profile import forms as participant_profile_forms

@permission_required('users.is_staff')
def dashboard(request):

    participant = Participant.objects.all().count()

    context = {
        'participant_profile': ParticipantProfile.objects.all(),
        'total_participant': participant,
    }

    return render(request, 'dashboard/dashboard.html', context)

@permission_required('users.is_staff')
def insert_participant(request):
    if request.method == 'POST':
        form = forms.RegisterStudentForm(request.POST)
        if form.is_valid():
            registration_number = register_number_generator()
            form_field = form.save(commit=False)

            password = form.cleaned_data['password']
            full_name = form.cleaned_data['full_name']
            user = CustomUser.objects.create_user(registration_number, password)

            form_field.registration_number = registration_number
            form.instance.account = user

            form.save(commit=True)
            user.save()

            context = {
                'success': True,
                'registration_number': registration_number,
                'password': password,
                'full_name': full_name,
            }
            return render(request, 'dashboard/insert_participant.html', context)
        else:
            return render(request, 'dashboard/insert_participant.html', context={'success': False, 'form': form})

    context = {
        'form': forms.RegisterStudentForm,
    }
    return render(request, 'dashboard/insert_participant.html', context)

# REGISTER SCHEDULE VIEW
class RegisterScheduleListView(UserIsStaffMixin, ListView):
    template_name = 'dashboard/registerschedule_list.html'
    model = RegisterSchedule

class RegisterScheduleCreateView(UserIsStaffMixin, CreateView):
    model = RegisterSchedule
    form_class = forms.RegisterScheduleForm
    template_name = "dashboard/registerschedule_form.html"
    success_url = reverse_lazy('register-schedule')

class RegisterSchduleDeleteView(UserIsStaffMixin, DeleteView):
    model = RegisterSchedule
    success_url = reverse_lazy('register-schedule')

class RegisterSchduleUpdateView(UserIsStaffMixin, UpdateView):
    model = RegisterSchedule
    form_class = forms.RegisterScheduleForm
    template_name = "dashboard/registerschedule_form.html"
    success_url = reverse_lazy('register-schedule')

# REGISTER STEP VIEW
class RegisterStepListView(UserIsStaffMixin, ListView):
    template_name = 'dashoard/registerstep_list.html'
    model = RegisterStep

class RegisterStepCreateView(UserIsStaffMixin, CreateView):
    model = RegisterStep
    form_class = forms.RegisterStepForm
    template_name = "dashboard/registerstep_form.html"
    success_url = reverse_lazy('register-step')

# PARTICIPANT PROFILE VIEW
class ParticipantBaseView(UserIsStaffMixin, View):
    form_class = None
    model = None
    template_name = "dashboard/participant_detail.html"
    success_url_name = 'participant-detail'
    is_account = False
    name = None

    def _get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy(self.success_url_name, kwargs={'pk': pk})

    def get(self, request, *args, **kwargs):
        # Taking primary key from url
        pk = self.kwargs.get('pk') # is this safe? if not pls fix it for me, ty

        try:
            data = self.model.objects.get(participant=pk)
            form = self.form_class(instance=data)
        except FieldError:
            try:
                data = self.model.objects.get(account=pk)
                form = self.form_class(instance=data)
            except self.model.DoesNotExist:
                form = self.form_class()
        except self.model.DoesNotExist:
            form = self.form_class()

        context = {
            'form': form,
            'is_account': self.is_account,
            'participant_name': CustomUser.objects.get(pk=pk),
            'text': self.name,
            'pk': pk,
        }
        return render(request, self.template_name, context)

    def _set_form_instance(self, request, data=None):
        if data:
            form = self.form_class(request.POST, request.FILES or None, instance=data)
        else:
            form = self.form_class(request.POST, request.FILES or None)

        return form

    def post(self, request, *args, **kwargs):
        # Taking primary key from url
        pk = self.kwargs.get('pk') # is this safe? if not pls fix it for me, ty

        try:
            data = self.model.objects.get(participant=pk)
            form = self._set_form_instance(request, data)
        except FieldError:
            try:
                data = self.model.objects.get(account=pk)
                form = self._set_form_instance(request, data)
            except self.model.DoesNotExist:
                data = CustomUser.objects.get(pk=pk)
                form = self._set_form_instance(request)
                form.instance.participant = data
        except self.model.DoesNotExist:
            data = CustomUser.objects.get(pk=pk)
            form = self._set_form_instance(request)
            form.instance.participant = data

        if form.is_valid():
            form.save()
            return redirect(self._get_success_url())

        context = {
            'form': form,
            'is_account': self.is_account,
            'participant_name': CustomUser.objects.get(pk=pk),
            'text': self.name,
            'pk': pk,
        }
        return render(request, self.template_name, context)

class ParticipantUpdateView(ParticipantBaseView):
    model = Participant
    form_class = forms.RegisterStudentFormDashboard
    success_url_name = 'participant-detail'
    name = 'Peserta'

class ParticipantProfileView(ParticipantBaseView):
    model = ParticipantProfile
    form_class = participant_profile_forms.ParticipantProfileForm
    success_url_name = 'participant-profile'
    name = 'Profile Peserta'

class ParticipantFatherProfileView(ParticipantUpdateView):
    model = FatherStudentProfile
    form_class = forms.FatherParticipantDashboardForm
    success_url_name = 'participant-father'
    name = 'Ayah Peserta'

class ParticipantMotherProfileView(ParticipantUpdateView):
    model = MotherStudentProfile
    form_class = forms.MotherParticipantDashboardForm
    success_url_name = 'participant-mother'
    name = 'Ibu Peserta'

class ParticipantGuardianProfile(ParticipantBaseView):
    model = StudentGuardianProfile
    form_class = forms.GuardianParticipantDashboardForm
    success_url_name = 'participant-guardian'
    name = 'Wali Peserta'

class ParticipantFilesView(ParticipantBaseView):
    model = StudentFile
    form_class = forms.ParticipantFilesDashboardForm
    success_url_name = 'participant-files'
    name = 'Berkas Peserta'

class ParticipantMajorView(ParticipantBaseView):
    model = MajorStudent
    form_class = forms.ParticipantMajorDashboard
    success_url_name = 'participant-major'
    name = 'Jurusan Pilihan Peserta'

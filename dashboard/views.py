import os
from io import BytesIO
import zipfile

from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.core.exceptions import FieldError, ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import PasswordChangeView
from django.conf import settings

from users.models import CustomUser
from users.mixins import UserIsStaffMixin

from excel_response import ExcelResponse
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from . import forms
from .models import (
    ParticipantCount, RegisterSchedule,
    RegisterStep, Participant, ParticipantGraduation,
    ParticipantLMS, ParticipantRePayment, InfoSourcePPDB,
)
from .generator import register_number_generator, reset_register_number

from participant_profile.models import (
    ParticipantProfile, MotherStudentProfile,
    FatherStudentProfile, StudentGuardianProfile,
    StudentFile, MajorStudent, PaymentUpload, ParticipantFamilyCert
)
from participant_profile import forms as participant_profile_forms


@permission_required('users.is_staff')
def dashboard(request):

    participant = Participant.objects.all()
    profile = ParticipantProfile.objects.all()
    passed_test = ParticipantGraduation.objects.all().count()

    verified = participant.filter(verified=True).count()
    not_verified = participant.count() - verified

    context = {
        'participant': participant,
        'part_count': participant.count(),
        'not_verified': not_verified,
        'verified': verified,
        'passed_test': passed_test,
    }

    return render(request, 'dashboard/dashboard.html', context)

@permission_required('users.is_staff')
def get_register_number(request):
    if request.method == 'POST':
        register_number = register_number_generator()
        return JsonResponse({'reg_num': register_number})

    raise PermissionDenied

@permission_required('users.is_staff')
def reset_registration_number(request):

    if request.method == 'POST':
        berhasil = reset_register_number()

        if berhasil:
            messages.success(request, 'Berhasil Me-Reset Nomor Pendaftaran.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Gagal Me-reset Nomor Pendaftaran.')
            return redirect('dashboard')

    return render(request, 'dashboard/reset_registration_number.html')

@permission_required('users.is_staff')
def insert_participant(request):
    if request.method == 'POST':
        form = forms.RegisterStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form_field = form.save(commit=False)

            password = form.cleaned_data['password']
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['participant_phone_number']
            user = CustomUser.objects.create_user(phone_number, password)

            form.instance.account = user

            form.save(commit=True)
            form.save_m2m()
            user.save()

            context = {
                'success': True,
                'password': password,
                'phone_number': phone_number,
                'full_name': full_name,
            }
            return render(request, 'dashboard/insert_participant.html', context)
        else:
            return render(request, 'dashboard/insert_participant.html', context={'success': False, 'form': form})

    context = {
        'form': forms.RegisterStudentForm,
    }
    return render(request, 'dashboard/insert_participant.html', context)


@permission_required('users.is_staff')
def files_download(request, pk):
    participant = Participant.objects.get(account=pk)

    fbuffer = BytesIO()
    path = f'{settings.MEDIA_ROOT}/berkas_{participant.account.username}/'
    files = os.listdir(path=path)

    zf = zipfile.ZipFile(fbuffer, "w")
    os.chdir(path)

    for fname in files:
        zf.write(f'{fname}')

    zf.close()

    resp = HttpResponse(fbuffer.getvalue(), headers={
        'Content-Type': "application/x-zip-compressed",
        'Content-Disposition': f'attachment; filename="Berkas_{participant.full_name}.zip"',
    })

    return resp

def analytic_view(request):
    info = InfoSourcePPDB.objects.all()

    label = []
    data = []
    for i in info:
        label.append(i.info_source) # Label
        data.append(i.participant_set.count()) # vote count

    return render(request, 'dashboard/analytic.html', {'data_list': [label, data], 'info': zip(data, label)})

class ExportToExcel(UserIsStaffMixin, View):
    model = None
    file_name = 'Data PPDB'

    def get(self, request, *args, **kwargs):
        ctx = {
            'export': [
                {
                    'title': 'Data Peserta',
                    'link': reverse('export-participant'),
                },
                {
                    'title': 'Data Ayah',
                    'link': reverse('export-father'),
                },
                {
                    'title': 'Data Ibu',
                    'link': reverse('export-mother'),
                },
                {
                    'title': 'Data Wali',
                    'link': reverse('export-guardian'),
                },
                {
                    'title': 'Data Jurusan Peserta',
                    'link': reverse('export-major'),
                },
            ]
        }
        return render(request, 'dashboard/export.html', ctx)

    def post(self, request, *args, **kwargs):
        PARTICIPANT = list(Participant.objects.values_list('registration_number', 'full_name'))
        PARTICIPANT_PROFILE = [
            x for x in self.model.objects.values_list(*[i.name for i in self.model._meta.fields[3:]])
        ]

        for a in range(1, len(PARTICIPANT)+1):
            try:
                PARTICIPANT[a-1] = list(PARTICIPANT[a-1])
                PARTICIPANT[a-1] += (PARTICIPANT_PROFILE[a-1])
            except IndexError:
                continue

        column = ['No. Pendaftaran', 'Nama Lengkap']
        column += [i.verbose_name for i in self.model._meta.fields[3:]]
        data = [column]

        data += PARTICIPANT
        return ExcelResponse(data, self.file_name)

class ExExcelParticipant(ExportToExcel):
    model = ParticipantProfile
    file_name = 'Data Peserta PPDB'

class ExExcelFather(ExportToExcel):
    model = FatherStudentProfile
    file_name = 'Data Ayah Peserta PPDB'

class ExExcelMother(ExportToExcel):
    model = MotherStudentProfile
    file_name = 'Data Ibu Peserta PPDB'

class ExExcelGuardian(ExportToExcel):
    model = StudentGuardianProfile
    file_name = 'Data Wali Peserta PPDB'

class ExExcelMajor(ExportToExcel):
    model = MajorStudent
    file_name = 'Data Jurusan Pilihan Peserta PPDB'

class ParticipantDeleteView(UserIsStaffMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('dashboard')

class PasswordChangeViewDashboard(UserIsStaffMixin, View):
    template_name = 'dashboard/participant_detail.html'
    success_url = 'participant-detail'
    form_class = forms.SetPasswordDashboardForm
    is_verify = False
    name = 'Password'

    def _get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.kwargs['pk']})

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        user = CustomUser.objects.get(pk=pk)

        context = {
            'pk': pk,
            'form': self.form_class(),
            'is_verify': self.is_verify,
            'participant_name': CustomUser.objects.get(pk=pk),
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        user = CustomUser.objects.get(pk=pk)
        form = self.form_class(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect(self._get_success_url())

        return render(request, self.template_name, {'pk': pk, 'form': form, 'is_verify': self.is_verify})


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

class RegisterStepDeleteView(UserIsStaffMixin, DeleteView):
    model = RegisterStep
    success_url = reverse_lazy('register-step')

class RegisterStepUpdateView(UserIsStaffMixin, UpdateView):
    model = RegisterStep
    form_class = forms.RegisterStepForm
    template_name = "dashboard/registerstep_form.html"
    success_url = reverse_lazy('register-step')

# INFO SOURCE PPDB
class InfoSourcePPDBView(UserIsStaffMixin, ListView):
    model = InfoSourcePPDB
    template_name = 'dashboard/infoppdb_list.html'

class InfoSourcePPDBDelete(UserIsStaffMixin, DeleteView):
    model = InfoSourcePPDB
    success_url = reverse_lazy('info-ppdb')

class InfoSourcePPDBCreate(UserIsStaffMixin, CreateView):
    model = InfoSourcePPDB
    form_class = forms.InfoSourcePPDBForm
    template_name = "dashboard/infoppdb_form.html"
    success_url = reverse_lazy('info-ppdb')

class InfoSourcePPDBUpdate(UserIsStaffMixin, UpdateView):
    model = InfoSourcePPDB
    form_class = forms.InfoSourcePPDBForm
    template_name = "dashboard/infoppdb_form.html"
    success_url = reverse_lazy('info-ppdb')

# PARTICIPANT PROFILE VIEW
class ParticipantBaseView(UserIsStaffMixin, View):
    form_class = None
    model = None
    template_name = "dashboard/participant_detail.html"
    success_url_name = 'participant-detail'
    is_account = False
    is_verify = True
    is_media = False
    name = None

    def _get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy(self.success_url_name, kwargs={'pk': pk})

    def _get_context(self, pk, form=None):
        return {
            'form': form,
            'is_account': self.is_account,
            'participant_name': CustomUser.objects.get(pk=pk),
            'text': self.name,
            'pk': pk,
            'is_media': self.is_media,
            'is_verify': self.is_verify,
        }

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

        return render(request, self.template_name, self._get_context(pk, form))

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
            messages.success(request, f'Data {self.name} berhasil di update.')
            return redirect(self._get_success_url())
            # return render(request, self.template_name, self._get_context(pk, form))

        return render(request, self.template_name, self._get_context(pk, form))

class ParticipantUpdateView(ParticipantBaseView):
    model = Participant
    form_class = forms.RegisterStudentFormDashboard
    success_url_name = 'participant-detail'
    name = 'Akun Peserta'
    is_media = True
    is_verify = True
    is_account = True

class ParticipantProfileView(ParticipantBaseView):
    model = ParticipantProfile
    form_class = forms.ParticipantProfileDashboardForm
    success_url_name = 'participant-profile'
    name = 'Profile Peserta'

class ParticipantFatherProfileView(ParticipantBaseView):
    model = FatherStudentProfile
    form_class = forms.FatherParticipantDashboardForm
    success_url_name = 'participant-father'
    name = 'Ayah Peserta'

class ParticipantMotherProfileView(ParticipantBaseView):
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
    is_verify = True
    is_media = True

class ParticipantMajorView(ParticipantBaseView):
    model = MajorStudent
    form_class = forms.ParticipantMajorDashboard
    success_url_name = 'participant-major'
    name = 'Jurusan Pilihan Peserta'

class ParticipantGradiationView(ParticipantBaseView):
    model = ParticipantGraduation
    form_class = forms.ParticipantGraduationForm
    success_url_name = 'participant-graduation'
    is_media = True
    name = 'Kelulusan'

class ParticipantLMSView(ParticipantBaseView):
    model = ParticipantLMS
    form_class = forms.ParticipantLMSAccountForm
    success_url_name = 'participant-lms'
    name = 'Akun LMS'

class ParticipantPaymentDashboardView(ParticipantBaseView):
    model = PaymentUpload
    form_class = forms.ParticipantPaymentDashboardForm
    success_url_name = 'participant-payment'
    name = 'Pembayaran Daftar Ulang'
    is_media = True

class RePaymentDView(ParticipantBaseView):
    model = ParticipantRePayment
    form_class = forms.ParticipantRePaymentForm
    success_url_name = 'participant-payment'
    name = 'Pembayaran Daftar Ulang'
    is_media = True

class ParticipantFamilyCertView(ParticipantBaseView):
    model = ParticipantFamilyCert
    form_class = forms.ParticipantFamilyCertForm
    success_url_name = 'participant-family-cert'
    name = 'Kartu Keluarga'
    is_media = True

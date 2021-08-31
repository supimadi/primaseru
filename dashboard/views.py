import os
from io import BytesIO
import zipfile

from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.core.exceptions import FieldError, ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import PasswordChangeView

from users.models import CustomUser
from users.mixins import UserIsStaffMixin


from excel_response import ExcelResponse

import xlsxwriter

from . import forms
from .models import (
    ParticipantCount, RegisterSchedule,
    RegisterStep, Participant, ParticipantGraduation,
    ParticipantLMS, ParticipantRePayment, InfoSourcePPDB,
    RegisterFilePrimaseru, ReRegisterFilePrimaseru, PaymentBanner,
    PrimaseruContacts
)
from .generator import register_number_generator, reset_register_number

from participant_profile.models import (
    ParticipantProfile, MotherStudentProfile,
    FatherStudentProfile, StudentGuardianProfile,
    StudentFile, MajorStudent, PaymentUpload,
    ParticipantFamilyCert, ReportFileParticipant
)
from participant_profile import forms as participant_profile_forms

from homepage.models import FilesPool


def dashboard(request):

    if not request.user.username in settings.ALLOW_VIEW_DASHBOARD_DUMMY:
        raise PermissionDenied

    participant = Participant.objects.all()
    profile = ParticipantProfile.objects.all()
    passed_test = ParticipantGraduation.objects.all().count()
    payment = ParticipantRePayment.objects.all()

    verified = participant.filter(verified=True).count()
    not_verified = participant.count() - verified

    context = {
        'participant': participant,
        'total_participant': participant.count(),
        'total_participant_accepted': passed_test,
        'total_participant_pay': payment.count(),
        'total_participant_paid_off': payment.filter(paid_off=True).count(),
        'total_participant_profile': profile.count(),
    }

    return render(request, 'dashboard/dashboard.html', context)

@permission_required('users.is_staff')
def verified_raport(request):

    if request.method == 'POST':
        pk = request.POST.get('primary_key')
        raport = ReportFileParticipant.objects.get(pk=pk)

        if raport.verified:
            raport.verified = False
        else:
            raport.verified = True

        raport.save()
        return JsonResponse({'success': True})

    raise PermissionDenied


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

    try:
        files = os.listdir(path=path)
    except FileNotFoundError:
        messages.warning(request, 'Tidak Ada Folder atau File.')
        return redirect('participant-detail', pk=pk)

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

@permission_required('users.is_staff')
def export_to_excel(request):
    fbuffer = BytesIO()
    workbook = xlsxwriter.Workbook(fbuffer)

    ws1 = workbook.add_worksheet('Data Peserta')
    ws2 = workbook.add_worksheet('Profile Peserta')
    ws3 = workbook.add_worksheet('Profile Ayah')
    ws4 = workbook.add_worksheet('Profile Ibu')
    ws5 = workbook.add_worksheet('Profile Wali')
    ws6 = workbook.add_worksheet('Jurusan Peserta')
    ws7 = workbook.add_worksheet('Sumber Info PPDB')


    name_list = Participant.objects.values_list('full_name', 'account')
    info_source = InfoSourcePPDB.objects.all()

    model_worksheet = [
        [Participant.objects.all(),False, ws1],
        [ParticipantProfile.objects.all(),True, ws2],
        [FatherStudentProfile.objects.all(),True, ws3],
        [MotherStudentProfile.objects.all(),True, ws4],
        [StudentGuardianProfile.objects.all(),True, ws5],
        [MajorStudent.objects.all(),True, ws6],
    ]

    def set_header(data):
        header_list = []
        try:
            for f in data.first()._meta.fields:
                header_list.append(f.verbose_name)
        except Exception:
            header_list = 'Tidak Ada Data!'

        return header_list

    def write_data(worksheet, data, header, add_name=False):
        if header == 'Tidak Ada Data!':
            worksheet.write(0,0, str(header))
        else:
            row = 0
            if add_name:
                worksheet.write(row,0, 'Nama Peserta')
                for name in name_list:
                    worksheet.write(row+1, 0, name[0])

                    for value in data.values():

                        col = 1
                        if not value['participant_id'] == name[1]:
                            continue

                        for v in value.values():
                            worksheet.write(row+1, col, v)
                            col += 1
                    row += 1

                col = 1 if add_name else 0
                for h in header:
                    worksheet.write(0, col, str(h))
                    col += 1
            else:
                col = 0
                for h in header:
                    worksheet.write(0, col, str(h))
                    col += 1

                row = 1
                for value in data.values():
                    col = 0
                    for v in value.values():
                        worksheet.write(row, col, str(v))
                        col += 1

                    row += 1


    info_sorce_header = ['Sumber Info PPDB', 'Jumlah Voting']
    data_info_source = []
    label_info_source = []
    for i in info_source:
        data_info_source.append(i.participant_set.count())
        label_info_source.append(i.info_source)

    row = 1
    for l,d in zip(label_info_source, data_info_source):
        ws7.write(row, 0, l)
        ws7.write(row, 1, d)
        row += 1

    col = 0
    for h in info_sorce_header:
        ws7.write(0, col, h)
        col += 1

    # data_header = set_header(model_worksheet[5][0])
    # data_values = model_worksheet[5][0].values()
    # write_data(model_worksheet[5][2], data_values, data_header, add_name=True)

    for mw in model_worksheet:
        data_header = set_header(mw[0])
        data_values = mw[0].values()

        if mw[1]:
            write_data(mw[2], data_values, data_header, add_name=True)
        else:
            write_data(mw[2], data_values, data_header)

    workbook.close()
    resp = HttpResponse(fbuffer.getvalue(), headers={
        'Content-Type': "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        'Content-Disposition': f'attachment; filename="Primaseru.xlsx"',
    })

    return resp

@permission_required('users.is_staff')
def analytic_view(request):
    info = InfoSourcePPDB.objects.all()

    label = []
    data = []
    for i in info:
        label.append(i.info_source) # Label
        data.append(i.participant_set.count()) # vote count

    return render(request, 'dashboard/analytic.html', {'data_list': [label, data], 'info': zip(data, label)})

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

# FILES POOL VIEW
class FilesPoolView(UserIsStaffMixin, ListView):
    model = FilesPool
    template_name = 'dashboard/filespool_list.html'

class FilesPoolDeleteView(UserIsStaffMixin, DeleteView):
    model = FilesPool
    success_url = reverse_lazy('files-pool')

class FilesPoolCreateView(UserIsStaffMixin, CreateView):
    model = FilesPool
    form_class = forms.FilesPoolForm
    template_name = 'dashboard/filespool_form.html'
    success_url = reverse_lazy('files-pool')

class FilesPoolUpdateView(UserIsStaffMixin, UpdateView):
    model = FilesPool
    form_class = forms.FilesPoolForm
    template_name = 'dashboard/filespool_form.html'
    success_url = reverse_lazy('files-pool')

# Register File View
class RegisterFileView(UserIsStaffMixin, ListView):
    model = RegisterFilePrimaseru
    template_name = 'dashboard/registerfiles_list.html'

class RegisterFileDeleteView(UserIsStaffMixin, DeleteView):
    model = RegisterFilePrimaseru
    success_url = reverse_lazy('files-register')

class RegisterFileUpdateView(UserIsStaffMixin, UpdateView):
    model = RegisterFilePrimaseru
    fields = '__all__'
    template_name = 'dashboard/registerfiles_form.html'
    success_url = reverse_lazy('files-register')

class RegisterFileCreateView(UserIsStaffMixin, CreateView):
    model = RegisterFilePrimaseru
    fields = '__all__'
    template_name = 'dashboard/registerfiles_form.html'
    success_url = reverse_lazy('files-register')

# Re Register File View
class ReRegisterFileView(UserIsStaffMixin, ListView):
    model = ReRegisterFilePrimaseru
    template_name = 'dashboard/reregisterfiles_list.html'

class ReRegisterFileDeleteView(UserIsStaffMixin, DeleteView):
    model = ReRegisterFilePrimaseru
    success_url = reverse_lazy('files-re-register')

class ReRegisterFileUpdateView(UserIsStaffMixin, UpdateView):
    model = ReRegisterFilePrimaseru
    fields = '__all__'
    template_name = 'dashboard/reregisterfiles_form.html'
    success_url = reverse_lazy('files-re-register')

class ReRegisterFileCreateView(UserIsStaffMixin, CreateView):
    model = ReRegisterFilePrimaseru
    fields = '__all__'
    template_name = 'dashboard/reregisterfiles_form.html'
    success_url = reverse_lazy('files-re-register')

# Re Register File View
class PrimaseruContactsView(UserIsStaffMixin, ListView):
    model = PrimaseruContacts
    template_name = 'dashboard/primaserucontacts_list.html'

class PrimaseruContactsDeleteView(UserIsStaffMixin, DeleteView):
    model = PrimaseruContacts
    success_url = reverse_lazy('primaseru-contacts')

class PrimaseruContactsUpdateView(UserIsStaffMixin, UpdateView):
    model = PrimaseruContacts
    fields = '__all__'
    template_name = 'dashboard/primaserucontacts_form.html'
    success_url = reverse_lazy('primaseru-contacts')

class PrimaseruContactsCreateView(UserIsStaffMixin, CreateView):
    model = PrimaseruContacts
    fields = '__all__'
    template_name = 'dashboard/primaserucontacts_form.html'
    success_url = reverse_lazy('primaseru-contacts')


# PAYMENT BANNER VIEW
class BannerPayment(UserIsStaffMixin, View):
    model = PaymentBanner
    form_class = forms.PaymentBannerForm
    template_name = 'dashboard/bannerpayment_form.html'

    def get(self, request, *args, **kwargs):

        try:
            data = self.model.objects.get(pk=1)
            form = self.form_class(instance=data)
        except self.model.DoesNotExist:
            form = self.form_class()
            data = None

        return render(request, self.template_name, {'data': data, 'form': form})

    def post(self, request, *args, **kwargs):

        try:
            data = self.model.objects.get(pk=1)
            form = self.form_class(request.POST, instance=data)
        except self.model.DoesNotExist:
            data = None
            form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil di-update.')
            return redirect("banner-payment")

        return render(request, self.template_name, {'data': data, 'form': form})


class RaportFilesView(UserIsStaffMixin, ListView):
    model = ReportFileParticipant
    template_name = 'dashboard/raport_list.html'
    context_object_name = "raport_files"

    def get_queryset(self):
        return self.model.objects.filter(participant=self.kwargs['account'])

    def get_context_data(self, **kwargs):
        pk = self.kwargs['account']
        context = super().get_context_data(**kwargs)
        context['pk'] = pk
        context['form_verify'] = forms.RaportFileVerifyForm
        context['participant_name'] = CustomUser.objects.get(pk=pk)

        return context

class RaportFileCreate(UserIsStaffMixin, CreateView):
    model = ReportFileParticipant
    form_class = forms.RaportFileDashboardForm
    template_name = "dashboard/participant_files.html"

    def get_success_url(self):
        return reverse('raport-list', kwargs={"account": self.kwargs['account']})

    def form_valid(self, form):
        account = CustomUser.objects.get(pk=self.kwargs['account'])
        form.instance.participant = account
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['account']
        context = super().get_context_data(**kwargs)
        context['pk'] = pk
        context['participant_name'] = CustomUser.objects.get(pk=pk)
        return context

class RaportFileDelete(UserIsStaffMixin, DeleteView):
    model = ReportFileParticipant

    def get_success_url(self):
        return reverse('raport-list', kwargs={"account": self.kwargs['account']})

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
    template_name = "dashboard/participant_files.html"
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
    template_name = "dashboard/participant_files.html"
    success_url_name = 'participant-family-cert'
    name = 'Kartu Keluarga'
    is_media = True

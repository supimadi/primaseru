from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


from . import models, forms
from .mixins import IsPassessTestPPDB

from dashboard.models import PaymentBanner

from dashboard.models import ParticipantGraduation, ParticipantLMS, Participant, ParticipantRePayment

@login_required
def index(request):
    if request.user.is_staff:
        return redirect('dashboard')

    if request.user.username in settings.ALLOW_VIEW_DASHBOARD_DUMMY:
        return redirect('dashboard')

    try:
        participant = Participant.objects.get(account=request.user.pk)
    except Participant.DoesNotExist:
        messages.warning(request, "Tidak dapat menemukan user")
        return redirect("login")

    if not participant.verified:
        data = PaymentBanner.objects.get(pk=1)
        return render(request, 'participant_profile/payment.html', {'data': data})

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

    try:
        data = Participant.objects.get(account=request.user.pk)
        image = models.PhotoProfile.objects.get(participant=request.user.pk)
    except Exception:
        messages.warning(request, 'Photo Belum diunggah!')
        return redirect('profile')

    return render(request, 'participant_profile/id_card_new.html', {'data': data, 'image': image})

@login_required
def skl_view(request):
    pk = request.user.pk

    data = get_object_or_404(Participant, account=pk)
    image = get_object_or_404(models.PhotoProfile, participant=pk)
    graduation = get_object_or_404(ParticipantGraduation, participant=pk)
    test = get_object_or_404(ParticipantLMS, participant=pk)

    ctx = {
        'data': data,
        'image': image,
        'graduation': graduation,
        'test': test,
    }


    return render(request, 'participant_profile/skl.html', ctx)

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
    form_class = None
    model = models.ParticipantProfile
    template_name = 'participant_profile/primaseru.html'
    url_name =  'participant-profile'
    name = 'peserta'
    multiple_files = False

    def _get_context(self, data, form, **kwargs):

        try:
            pay = ParticipantRePayment.objects.get(participant=self.request.user.pk).payment_1
        except ParticipantRePayment.DoesNotExist:
            pay = None

        try:
            passed = ParticipantGraduation.objects.get(participant=self.request.user.pk).passed
            graduation = ParticipantGraduation.objects.get(participant=self.request.user.pk)
        except ParticipantGraduation.DoesNotExist:
            graduation = None
            passed = None

        #  try:
        #      lms = ParticipantLMS.objects.get(participant=self.request.user.pk)
        #  except ParticipantLMS.DoesNotExist:
        #      lms = None

        ctx = {
            'form_ph': forms.PhotoProfileForm(),
            'form': form,
            'name': self.name,
            'data': data,
            'pay': pay,
            'lms': False,
            'graduation': graduation,
            'passed': passed,
            'multiple_files': self.multiple_files,
        }

        ctx.update(kwargs)
        return ctx

    def form_valid(self, request, *args, **kwargs):
        # TODO implement later for reperate logic
        pass

    def get(self, request, *args, **kwargs):

        try:

            if self.multiple_files:
                data = self.model.objects.filter(participant=request.user)
            else:
                data = self.model.objects.get(participant=request.user)

            form = self.form_class(instance=data) if self.form_class else None
        except self.model.DoesNotExist:
            data = None
            form = self.form_class() if self.form_class else None

        return render(request, self.template_name, self._get_context(data, form))

    def post(self, request, *args, **kwargs):

        try:

            data = None # when multiple files we assume no instance will attached
            if not self.multiple_files:
                data = self.model.objects.get(participant=request.user)

            form = self.form_class(request.POST, request.FILES or None, instance=data)

        except (self.model.DoesNotExist, ValueError):
            data = None
            form = self.form_class(request.POST, request.FILES or None)

        if form.is_valid():
            form.save(commit=False)
            form.instance.participant = request.user

            form.save(commit=True)
            messages.success(request, f'Data {self.name} berhasil di upload.')
            return redirect(self.url_name)

        return render(request, self.template_name, self._get_context(data, form))

class ParticipantProfileView(ProfileView):
    form_class = forms.ParticipantProfileForm
    model = models.ParticipantProfile
    template_name = 'participant_profile/primaseru.html'
    url_name =  'participant-profile'
    name = 'peserta'

class FatherProfileView(ProfileView):
    form_class = forms.FatherParticipantForm
    model = models.FatherStudentProfile
    url_name = 'participant-father'
    name = "ayah"

class MotherProfileView(ProfileView):
    form_class = forms.MotherParticipantForm
    model = models.MotherStudentProfile
    url_name = 'participant-mother'
    name = "ibu"

class GuardianProfileView(ProfileView):
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
    model = models.ParticipantFamilyCert
    url_name = 'participant-kk'
    # template_name = "participant_profile/participant_files.html"
    name = "Kartu Keluarga dan Akta Kelahiran"

    def get(self, request, *args, **kwargs):

        try:
            achiev = models.MajorStudent.objects.get(participant=request.user)
        except models.MajorStudent.DoesNotExist:
            messages.warning(request, "Harap memilih jurusan terlebih dahulu.")
            return redirect("participant-major")

        try:

            if self.multiple_files:
                data = self.model.objects.filter(participant=request.user)
            else:
                data = self.model.objects.get(participant=request.user)

            form = self.form_class(instance=data)
        except self.model.DoesNotExist:
            data = None
            form = self.form_class()


        return render(request, self.template_name, self._get_context(data, form, achiev=achiev.way_in))

class CertProfileView(ProfileView):
    model = models.ParticipantCert
    form_class = forms.ParticipantCertForm
    url_name = 'participant-cert'
    template_name = "participant_profile/participant_cert.html"
    name = 'Sertifikat Penghargaan'
    multiple_files = True

    def get(self, request, *args, **kwargs):

        try:
            achiev = models.MajorStudent.objects.get(participant=request.user)
        except models.MajorStudent.DoesNotExist:
            messages.warning(request, "Harap memilih jurusan terlebih dahulu.")
            return redirect("participant-major")

        # just a student with 'Jalur Pestasi' may pass
        if not achiev.way_in == 'Jalur Prestasi':
            messages.warning(request, "Unggah Sertifikat Penghargaan, hanya untuk jalur prestasi.")
            return redirect("participant-major")

        data = self.model.objects.filter(participant=request.user)
        form = self.form_class()

        return render(request, self.template_name, self._get_context(data, form, achiev=achiev.way_in))


class ParticipantLMSAccount(ProfileView):
    model = ParticipantLMS
    url_name = 'participant-lms'
    template_name = "participant_profile/lms_account.html"
    name = "Test Minat Bakat"

class ParticipantGraduationView(ProfileView):
    model = ParticipantGraduation
    url_name = 'participant-graduation'
    template_name = "participant_profile/graduation.html"
    name = 'Kelulusan'

class RePaymentPage(IsPassessTestPPDB, ProfileView):
    model = ParticipantRePayment
    form_class = forms.ParticipantRePaymentForm
    url_name = 'participant-payment'
    template_name = "participant_profile/re_payment.html"
    name = 'Pembayaran Daftar Ulang'

class RaportParticipantView(IsPassessTestPPDB, ProfileView):
    model = models.ReportFileParticipant
    form_class = forms.ParticipantRaportForm
    url_name = 'participant-raport'
    template_name = "participant_profile/raport_files.html"
    name = 'Berkas Raport'
    multiple_files = True

    def get(self, request, *args, **kwargs):

        achiev = models.MajorStudent.objects.get(participant=request.user)

        data = self.model.objects.filter(participant=request.user)
        form = self.form_class()

        return render(request, self.template_name, self._get_context(data, form, achiev=achiev.way_in))


class ParticipantRaportDeleteView(UserPassesTestMixin, DeleteView):
    model = models.ReportFileParticipant
    success_url = reverse_lazy('participant-raport')

    def test_func(self):
        obj =  self.model.objects.get(pk=self.kwargs['pk'])

        # check if the logged user is the author
        # of the file
        if obj.participant.pk == self.request.user.pk:
            return True

        return False

class ParticipantCertDelete(UserPassesTestMixin, DeleteView):
    model = models.ParticipantCert
    success_url = reverse_lazy("participant-cert")

    def test_func(self):
        obj =  self.model.objects.get(pk=self.kwargs['pk'])

        # check if the logged user is the author
        # of the file
        if obj.participant.pk == self.request.user.pk:
            return True

        return False

class ParticipantFilesView(IsPassessTestPPDB, ProfileView):
    model = models.StudentFile
    form_class = forms.ParticipantFilesForm
    url_name = 'participant-files'
    template_name = "participant_profile/participant_files.html"
    name = 'Upload Berkas Penting Lainnya'

    def get(self, request, *args, **kwargs):

        achiev = models.MajorStudent.objects.get(participant=request.user)
        try:

            if self.multiple_files:
                data = self.model.objects.filter(participant=request.user)
            else:
                data = self.model.objects.get(participant=request.user)

            form = self.form_class(instance=data)
        except self.model.DoesNotExist:
            data = None
            form = self.form_class()

        return render(request, self.template_name, self._get_context(data, form, achiev=achiev.way_in))

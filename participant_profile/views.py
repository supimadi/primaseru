from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.template.context_processors import csrf

from crispy_forms.utils import render_crispy_form

from . import models, forms


def index(request):
    return render(request, 'participant_profile/primaseru.html')

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
        # if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        #     raise PermissionDenied

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
            form = self.form_class(request.POST, instance=data)

            if data.verified:
                return JsonResponse({'success': False}, status=403)

        except self.model.DoesNotExist:
            form = self.form_class(request.POST)
            form.save(commit=False)
            form.instance.participant = request.user

        ctx = {}
        ctx.update(csrf(request))

        if form.is_valid():
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

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.utils import timezone
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


from users.models import CustomUser
from users.mixins import UserIsStaffMixin

from .forms import RegisterStudentForm, RegisterScheduleForm
from .models import ParticipantCount, RegisterSchedule
from .generator import register_number_generator

@permission_required('users.is_staff')
def dashboard(request):
    context = {
        'form': RegisterStudentForm
    }

    return render(request, 'dashboard/dashboard.html', context)

@permission_required('users.is_staff')
def insert_participant(request):
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
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

    context = {
        'form': RegisterStudentForm,
    }
    return render(request, 'dashboard/insert_participant.html', context)

class RegisterScheduleListView(UserIsStaffMixin, ListView):
    template_name = 'dashboard/registerschedule_list.html'
    model = RegisterSchedule

class RegisterScheduleCreateView(UserIsStaffMixin, CreateView):
    model = RegisterSchedule
    form_class = RegisterScheduleForm
    template_name = "dashboard/registerschedule_form.html"
    success_url = '/d/j/pendaftaran/'

class RegisterSchduleDeleteView(UserIsStaffMixin, DeleteView):
    model = RegisterSchedule
    success_url = '/d/j/pendaftaran/'

class RegisterSchduleUpdateView(UserIsStaffMixin, UpdateView):
    model = RegisterSchedule
    form_class = RegisterScheduleForm
    template_name = "dashboard/registerschedule_form.html"
    success_url = '/d/j/pendaftaran/'

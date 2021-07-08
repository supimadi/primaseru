from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone

from .forms import RegisterStudentForm
from users.models import CustomUser
from .models import ParticipantCount

@login_required
def dashboard(request):

    context = {
        'form': RegisterStudentForm
    }

    return render(request, 'dashboard/dashboard.html', context)

def register_number_generator():
    year_today = timezone.now()
    year_today.year
    year_today = [y for y in str(year_today.year)]
    year_today.remove('0')

    try:
        obj = ParticipantCount.objects.get(pk=1)
    except Person.DoesNotExist:
        obj = ParticipantCount(count='001')
        obj.save()

    registration_number = "".join(map(str, year_today)) + str(obj.count)
    obj.count = "{0:03}".format(int(obj.count) + 1)
    obj.save()

    return registration_number


def insert_participant(request):

    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            registration_number = register_number_generator()
            form_field = form.save(commit=False)

            user = CustomUser.objects.create_user(registration_number, form.cleaned_data['password'])
            password = form.cleaned_data['password']

            form_field.registration_number = registration_number
            form.instance.account = user

            form.save(commit=True)
            user.save()

            context = {
                'success': True,
                'registration_number': registration_number,
                'password': password,
            }
            return render(request, 'dashboard/insert_participant.html', context)


    context = {
        'form': RegisterStudentForm,
    }
    return render(request, 'dashboard/insert_participant.html', context)

from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from . import forms
from users.models import CustomUser
from dashboard.models import Participant
from dashboard.generator import register_number_generator


def home(request):
    return render(request, 'homepage/home.html')

def register(request):
    form = forms.UserRegisterForm()
    form2 = forms.ParticipantRegisterForm()

    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        form2 = forms.ParticipantRegisterForm(request.POST)

        if form.is_valid() and form2.is_valid():
            register_number = register_number_generator()

            CustomUser.objects.create_user(register_number, form.cleaned_data['password2'])
            user = authenticate(request, username=register_number, password=form.cleaned_data['password2'])

            if user is not None:
                login(request, user) # Attach user to session

                # Save some data to session
                request.session['date_born'] = form2.cleaned_data['date_born'].strftime('%d/%m/%Y')
                request.session['place_born'] = form2.cleaned_data['place_born']
                request.session['school'] = form2.cleaned_data['school']

                participant = Participant.objects.create(
                    full_name=form2.cleaned_data['full_name'],
                    account=request.user,
                    registration_number=register_number,
                    participant_phone_number=form2.cleaned_data['participant_phone_number'],
                    homeroom_teacher_phone_number=form2.cleaned_data['homeroom_teacher_phone_number'],
                    parent_phone_number=form2.cleaned_data['parent_phone_number'],
                )
                participant.save()

                return redirect('initial-form')

    ctx = {
        'form': form,
        'form2': form2,
    }
    return render(request, 'homepage/register.html', ctx)

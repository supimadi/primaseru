from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from . import forms, models

from dashboard.models import PaymentBanner, PrimaseruContacts

from users.models import CustomUser
from dashboard.models import Participant, RegisterSchedule, RegisterStep, RegisterFilePrimaseru, ReRegisterFilePrimaseru
from dashboard.generator import register_number_generator

def download_menu(request):
    files = models.FilesPool.objects.all()

    return render(request, 'homepage/download-menu.html', {'files': files})

def home(request):
    ctx = {
        'schedule': RegisterSchedule.objects.all(),
        'step': RegisterStep.objects.all(),
        'register_files': RegisterFilePrimaseru.objects.all(),
        're_register_files': ReRegisterFilePrimaseru.objects.all(),
        'banner': PaymentBanner.objects.get(pk=1),
    }
    return render(request, 'homepage/home.html', ctx)

def register(request):
    form = forms.UserRegisterForm()
    form2 = forms.ParticipantRegisterForm()

    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        form2 = forms.ParticipantRegisterForm(request.POST)

        if form.is_valid() and form2.is_valid():

            ctx = {
                'form': form,
                'form2': form2,
            }

            try:
                CustomUser.objects.create_user(form2.cleaned_data['participant_phone_number'], form.cleaned_data['password2'])
                user = authenticate(request, username=form2.cleaned_data['participant_phone_number'], password=form.cleaned_data['password2'])
            except Exception:
                messages.warning(request, 'Data Tidak Valid, Kemungkinan No. HP Telah Digunakan.')
                return render(request, 'homepage/register.html', ctx)

            if user is not None:
                login(request, user) # Attach user to session

                participant = Participant.objects.create(
                    full_name=form2.cleaned_data['full_name'],
                    account=request.user,
                    participant_phone_number=form2.cleaned_data['participant_phone_number'],
                    homeroom_teacher_phone_number=form2.cleaned_data['homeroom_teacher_phone_number'],
                    bk_teacher_phone_number=form2.cleaned_data['bk_teacher_phone_number'],
                    parent_phone_number=form2.cleaned_data['parent_phone_number'],
                    parent_full_name=form2.cleaned_data['parent_full_name'],
                    previous_school=form2.cleaned_data['school'],
                    # info=form2.cleaned_data['info']
                )
                participant.save()
                participant.info.set(form2.cleaned_data['info'])
                return redirect('profile')

    ctx = {
        'form': form,
        'form2': form2,
        'kontak': PrimaseruContacts.objects.all(),
    }
    return render(request, 'homepage/register.html', ctx)

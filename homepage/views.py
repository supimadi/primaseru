from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from . import forms, models

from users.models import CustomUser

from dashboard.models import (
    RegisterSchedule, RegisterStep,
    RegisterFilePrimaseru, ReRegisterFilePrimaseru,
    PaymentBanner, PrimaseruContacts
)


def download_menu(request):
    files = models.FilesPool.objects.all()

    return render(request, 'homepage/download-menu.html', {'files': files})

def home(request):
    ctx = {
        'schedule': RegisterSchedule.objects.all(),
        'step': RegisterStep.objects.all(),
        'register_files': RegisterFilePrimaseru.objects.all(),
        're_register_files': ReRegisterFilePrimaseru.objects.all(),
        'pros_telkom': models.ProsTelkomBandung.objects.all(),
        'banner': PaymentBanner.objects.get(pk=1),
        'testimoni': models.TestimonialModel.objects.all(),
    }
    return render(request, 'homepage/home.html', ctx)

def register(request):
    kontak = PrimaseruContacts.objects.all()

    # Draw form and ui
    if request.method != 'POST':
        ctx = {
            'form': forms.UserRegisterForm(),
            'form2': forms.ParticipantRegisterForm(),
            'kontak': kontak,
        }

        return render(request, 'homepage/register.html', ctx)

    form = forms.UserRegisterForm(request.POST)
    form2 = forms.ParticipantRegisterForm(request.POST)

    # If both form not valid, return it with
    # error message
    if not (form.is_valid() and form2.is_valid()):

        ctx = {'form': form, 'form2': form2, 'kontak': kontak}
        return render(request, 'homepage/register.html', ctx)

    username = form2.cleaned_data['participant_phone_number']
    password = form.cleaned_data['password2']

    try:
        CustomUser.objects.create_user(username=username, password=password)
        user = authenticate(request, username=username, password=password)
    except Exception as e:
        # return error when somthing wrong
        messages.warning(request, f'Data Tidak Valid, Kemungkinan No. HP Telah Digunakan. error: {e}')
        ctx = {'form': form, 'form2': form2, 'kontak': kontak}
        return render(request, 'homepage/register.html', ctx)

    login(request, user) # Attach user to session

    form_field = form2.save(commit=False)

    # Instancing newly created user with the 'profile'
    form2.instance.account = user

    form2.save(commit=True)
    form2.save_m2m()

    return redirect('profile')


def register_old(request):
    form = forms.UserRegisterForm()
    form2 = forms.ParticipantRegisterForm()

    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        form2 = forms.ParticipantRegisterForm(request.POST)

        if form.is_valid() and form2.is_valid():

            username = form2.cleaned_data['participant_phone_number']
            password = form.cleaned_data['password2']

            try:
                CustomUser.objects.create_user(username=username, password=password)
                user = authenticate(request, username=username, password=password)

            except Exception as e:
                messages.warning(request, f'Data Tidak Valid, Kemungkinan No. HP Telah Digunakan. error: {e}')
                return render(request, 'homepage/register.html', ctx)

            if user is not None:
                login(request, user) # Attach user to session
                form2 = forms.ParticipantRegisterForm(request.POST)

                account = form2.save(commit=False)
                account.account = user

                account.save()
                form2.save_m2m()

                # participant = Participant.objects.create(
                #     full_name=form2.cleaned_data['full_name'],
                #     account=request.user,
                #     participant_phone_number=form2.cleaned_data['participant_phone_number'],
                #     homeroom_teacher_phone_number=form2.cleaned_data['homeroom_teacher_phone_number'],
                #     bk_teacher_phone_number=form2.cleaned_data['bk_teacher_phone_number'],
                #     parent_phone_number=form2.cleaned_data['parent_phone_number'],
                #     parent_full_name=form2.cleaned_data['parent_full_name'],
                #     previous_school=form2.cleaned_data['school'],
                #     # info=form2.cleaned_data['info']
                # )
                # participant.save()
                # participant.info.set(form2.cleaned_data['info'])
                return redirect('profile')

    ctx = {
        'form': form,
        'form2': form2,
        'kontak': PrimaseruContacts.objects.all(),
    }
    return render(request, 'homepage/register.html', ctx)

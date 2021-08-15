class InitialFormView(View):
    form_classes = [ # Pairing the form with it model
        [
            initial_forms.ParticipantProfileForm,
            models.ParticipantProfile,
        ],
        [
            initial_forms.ParticipantAddressForm,
            models.ParticipantProfile,
        ],
        [
            initial_forms.ParticipantMedicalRecord,
            models.ParticipantProfile,
        ],
        [
            initial_forms.ParticipantParentProfileForm,
            models.FatherStudentProfile,
        ],
        [
            initial_forms.ParticipantParentProfileForm,
            models.MotherStudentProfile,
        ],
        [
            initial_forms.ParticipantParentProfileForm,
            models.StudentGuardianProfile,
        ],
        [
            initial_forms.MajorParticipantForm,
            models.MajorStudent,
        ],
    ]
    template_name = 'participant_profile/initial_form.html'

    # Check if user already filling the form
    def _check_done(self):
        try:
            data = models.MajorStudent.objects.get(participant=self.request.user.pk)
        except Exception:
            data = None

        done = self.request.session.get('finish-initial-form', False)

        if data or done:
            return True
        else:
            return False

    def get(self, request, *args, **kwargs):
        # Retrive or set a value to session

        if self._check_done():
            return redirect('profile')

        try:
            step = request.session['step']
        except KeyError:
            step = request.session['step'] = 1

        data = request.session.get(f'{step}_data')
        model = self.form_classes[step-1][1].__name__

        if model == 'StudentGuardianProfile':
            skipable = True
        else:
            skipable = False

        # If user click previous retrive
        # data from session
        try:
           if not 'previous' in data:
               initial = data
           else:
               initial = {'step': step, 'model': model}
        except Exception:
               initial = {'step': step, 'model': model}

        if step == 1:
            initial.update({
                'date_born': request.session.get('date_born'),
                'city_born': request.session.get('place_born'),
                'school_origin': request.session.get('school'),
            })

        form =  self.form_classes[step-1][0](initial=initial)
        return render(request, self.template_name, {'form': form, 'step': step, 'skipable': skipable})

    def _save_to_db(self, request):
        """
        Save form data from session to database
        """
        data = None
        for model in self.form_classes:
            # check if the data is the same as before
            try:
                if data == request.session[f'{model[1].__name__}_data']:
                    continue
                data = request.session[f'{model[1].__name__}_data']
            except KeyError:
                continue

            # Delete unnecessary keys and values
            try:
                del data['step']
                del data['model']
                del data['csrfmiddlewaretoken']
                data['date_born'] = datetime.datetime.strptime(data['date_born'], '%d/%m/%Y').strftime('%Y-%m-%d')
            except KeyError:
                pass
            # change date format and then save it to db
            data_model = model[1].objects.create(**data, participant_id=request.user.pk)
            data_model.save()
            request.session['finish-initial-form'] = True

    def _previous_form(self, request):
        """
        Just decrement step from session
        """
        step = request.session['step']

        if step == 1:
            return
        else:
            request.session["step"] -= 1

    def _skip_form(self, request):
        step = request.session['step']

        if step == 1:
            return
        else:
            request.session["step"] += 1

    def post(self, request, *args, **kwargs):
        step = request.session['step']
        if request.POST.get('step'):
            request.session[f'{step}_data'] = request.POST.dict()

        request.session['model'] = request.POST.get('model', None)
        form =  self.form_classes[step-1][0](request.POST)

        if request.POST.get('previous') == 'previous':
            self._previous_form(request)
            return redirect('initial-form')

        if request.POST.get('skip') == 'skip':
            self._skip_form(request)
            return redirect('initial-form')

        if not form.is_valid():
            return render(request, self.template_name, {'form': form, 'step': step})

        # create session for form data, or append to it when
        # the model name are the same
        try:
            request.session[f'{request.POST["model"]}_data'].update(request.POST.dict())
        except Exception:
            request.session[f'{request.POST["model"]}_data'] = request.POST.dict()

        # Check if step already max, save the form data to db
        if request.session['step'] == len(self.form_classes):
            self._save_to_db(request)
            return redirect('initial-photo')

        request.session['step'] += 1
        return redirect('initial-form')

@login_required
def initial_photo(request):
    form = forms.PhotoProfileForm()
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

    return render(request, 'participant_profile/initial_form_photo.html', {'form': form, 'step': 8})

from .models import ParticipantCount, Participant

def register_number_generator():
    try:
        obj = ParticipantCount.objects.get(pk=1)
    except ParticipantCount.DoesNotExist:
        return 'Set Dulu Nomor Pendaftaran!'

    year = [y for y in str(obj.year)]
    year.remove('0')

    while True:
        registration_number = "".join(map(str, year)) + str(obj.count)
        obj.count = "{0:03}".format(int(obj.count) + 1)
        obj.save()

        if not Participant.objects.filter(registration_number__contains=registration_number).exists():
            break

    return registration_number

def reset_register_number():

    try:
        count = ParticipantCount.objects.get(pk=1)
        count.count = '001'
        count.save()
    except Exception:
        return False

    return True

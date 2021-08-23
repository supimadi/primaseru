from .models import ParticipantCount, Participant
from django.utils import timezone

def register_number_generator():
    year_today = timezone.now()
    year_today.year
    year_today = [y for y in str(year_today.year)]
    year_today.remove('0')

    try:
        obj = ParticipantCount.objects.get(pk=1)
    except ParticipantCount.DoesNotExist:
        obj = ParticipantCount(count='001')
        obj.save()

    while True:
        registration_number = "".join(map(str, year_today)) + str(obj.count)
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

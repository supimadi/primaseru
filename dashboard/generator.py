from .models import ParticipantCount
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

    registration_number = "".join(map(str, year_today)) + str(obj.count)
    obj.count = "{0:03}".format(int(obj.count) + 1)
    obj.save()

    return registration_number

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from users.models import CustomUser

from dashboard.models import ParticipantGraduation, Participant
from .models import StudentFile


@receiver(post_save, sender=ParticipantGraduation)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.passed == 'L':
            # StudentProfile.objects.create(student=instance)
            # obj = StudentFile.objects.get(participant=instance.participant)
            # obj.verified = False
            # obj.save()
            pass

@receiver(post_save, sender=Participant)
def telegram_notif(sender, instance, created, **kwargs):
    if created:
        pass

@receiver(post_save, sender=Participant)
def change_username(sender, instance, **kwargs):
    user = CustomUser.objects.get(pk=instance.account.pk)
    user.username = instance.participant_phone_number
    user.save()

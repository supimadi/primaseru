from django.contrib.auth.mixins import UserPassesTestMixin

from dashboard.models import ParticipantGraduation

class IsPassessTestPPDB(UserPassesTestMixin):

    def test_func(self):
        data = ParticipantGraduation.objects.get(participant=self.request.user.pk)

        if data.passed == 'L':
            return True

        return False

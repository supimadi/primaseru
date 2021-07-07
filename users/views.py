from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin

from exam.models import Score

class UserIsStaffMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff

class PassEnrollMixin(UserPassesTestMixin):

    def test_func(self):
        pk_exam = self.kwargs['pk_exam']
        check_score = Score.objects.filter(student=self.request.user, exam=pk_exam).exists()

        granted = False
        if f'exam_{pk_exam}_enroll' in self.request.session:
             granted = True
        if check_score:
            granted = False
        if self.request.session.get(f'exam_{pk_exam}_times_up'):
            granted = False

        return granted

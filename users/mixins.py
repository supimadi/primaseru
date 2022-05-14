from django.contrib.auth.mixins import UserPassesTestMixin


class UserPermissionMixin(UserPassesTestMixin):
    is_granted = False
    def test_func(self):
        self.is_granted = False

        if self.request.user.is_superuser:
            self.is_granted = True
        
        return self.is_granted;

class UserIsStaffMixin(UserPermissionMixin):
    def test_func(self):
        if self.request.user.is_staff:
            self.is_granted = True
        return super().test_func()

class UserIsSuperUserMixin(UserPermissionMixin):
    def test_func(self):
        return super().test_func()

class UserIsVerifierMixin(UserPermissionMixin):
    def test_func(self):
        if self.request.user.is_verifier:
            return True

        return self.request.user.is_verifier 
 

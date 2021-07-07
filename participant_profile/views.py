from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core.exceptions import PermissionDenied


class ProfileView(LoginRequiredMixin, View):
    pass

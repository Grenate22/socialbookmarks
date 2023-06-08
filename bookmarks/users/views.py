from django.shortcuts import render
from django.urls import reverse , reverse_lazy
from bookmarks import settings
from django.views.generic.edit import CreateView, UpdateView
from allauth.account.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CustomLoginForm,ProfileEditForm
from .models import Profile

# Create your views here.

class CustomLoginView(CreateView):
    form_class = CustomLoginForm
    template_name = 'templates/account/login.html'

class CustomChangeView(PasswordChangeView):
    def get_success_url(self) -> str:
        success_url = reverse('settings')
        return super().get_success_url()

class UpdateProfileView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    form_class = ProfileEditForm
    model = Profile
    template_name = 'account/profile_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


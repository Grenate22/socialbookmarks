from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from .forms import ImageCreationForm
# Create your views here.
class ImageCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'images/image/create.html'
    form_class = ImageCreationForm
    success_message = "Image added successfully"

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_invalid(form)
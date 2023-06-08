from django.urls import path
from .views import UpdateProfileView

urlpatterns = [
    path('<slug:slug>', UpdateProfileView.as_view(), name='update_profile'),
]
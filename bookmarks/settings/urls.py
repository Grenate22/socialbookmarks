from django.urls import path
from .views import SettingHomeView

urlpatterns = [
    path('', SettingHomeView.as_view(), name='settings'),
]
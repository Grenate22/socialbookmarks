from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import perform_login
from .models import CustomUser

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id:
            return
        try :
            customer = CustomUser.objects.get(email=user.email) 
            sociallogin.state['process'] = 'connect'
            perform_login(request, customer, 'none')
        except CustomUser.DoesNotExist:
            pass
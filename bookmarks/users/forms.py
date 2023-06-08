from allauth.account.forms import LoginForm,SignupForm
from django import forms
from .models import CustomUser, Profile

class CustomSignup(SignupForm):
    def __init__(self,*args,**kwargs):
        super(CustomSignup,self).__init__(*args,**kwargs)
        self.fields['organization']=forms.CharField(widget=forms.TextInput(attrs={"placeholder": "organization", "autocomplete": "organization"}))
        
    def save(self, request):
        organization = self.cleaned_data.pop('organization')
        user = super(CustomSignup,self).save(request)



class CustomLoginForm(LoginForm):
    def __init__(self,*args,**kwargs):
        super(CustomLoginForm,self).__init__(*args,**kwargs)
        self.fields['password'].widget.attrs.update({'placeholder': 'Password',
                                                 'class': 'form-control',
                                                 'id': 'password',
                                                 'name' : 'password'
                                                 })
   

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',}))
    
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ['username','email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['website','facebook_url','twitter_url','instagram_url','linkedln_url','avatar','bio']

         



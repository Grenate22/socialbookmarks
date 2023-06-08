from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser,Profile
from .forms import CustomSignup,UpdateUserForm

class CustomUserAdmin(UserAdmin):
    add_form=CustomSignup
    form=UpdateUserForm
    model=CustomUser
    list_display= ['email','username','is_staff']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','avatar')
    prepopulated_fields = {"slug": ("user",)}
    raw_id_fields = ['user']

    def avatar(self,obj):
        if obj.image:
            return format_html('<img scr="{}" width="50" height="50" />', obj.image.url)
        else:
            return None
    avatar.short_description = "Image"

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify 
from PIL import Image

class CustomUser(AbstractUser):
    pass

class Profile (models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField()
    website = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(max_length=200,null=True,blank=True)
    twitter_url = models.URLField(max_length=200,null=True,blank=True)
    instagram_url = models.URLField(max_length=200,null=True,blank=True)
    linkedln_url = models.URLField(max_length=200,null=True,blank=True)
    avatar = models.ImageField(default='profile_pic/avatar.png', upload_to='profile_pic', blank=True)
    bio = models.TextField()

    def __str__(self) -> str:
        return f"profile of {self.user.username}"
    
    def get_absolute_url(self):
        return reverse("update_profile", args=[self.slug])
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        avatar = Image.open(self.avatar.path)  # Open image

        #resize image 
        if avatar.height> 300 or avatar.width > 300 :
            output_size = (300, 300)
            avatar.thumbnail(output_size) # Resize image
            avatar.save (self.avatar.path)  # Save it again and override the larger image

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
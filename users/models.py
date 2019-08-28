from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    intro_user = models.CharField(max_length=200, null=True)
    about_user = RichTextField()
    photo = models.ImageField(upload_to='images/%Y/%m/%d', null=True)

    def __str__(self):
        return self.user.username

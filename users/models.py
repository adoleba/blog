from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_user = models.TextField(null=True)
    intro_user = models.CharField(max_length=200,  null=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d', null=True)

    def __str__(self):
        return self.user.username

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    photo = models.ImageField(upload_to='images/%Y/%m/%d')

    def _str__(self):
        return self.user.username

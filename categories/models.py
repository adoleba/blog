from cloudinary.models import CloudinaryField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, null=True)
    photo = CloudinaryField('Photo', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category:category_posts', args=[self.slug])

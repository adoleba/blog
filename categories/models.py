from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True, null=True)

    def __str__(self):
        return self.name

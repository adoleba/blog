from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class PostCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=80)
    sub_title = models.CharField(max_length=200)
    category = models.ManyToManyField(PostCategory)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    main_photo = models.ImageField(upload_to='images/%Y/%m/%d')
    thumbnail_photo = models.ImageField(upload_to='images/%Y/%m/%d')
    intro = models.CharField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Opublikowany')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    def __str__(self):
        return self.title

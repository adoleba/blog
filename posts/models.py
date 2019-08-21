from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique_for_date='published', null=True)
    sub_title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    main_photo = models.ImageField(upload_to='images/%Y/%m/%d')
    thumbnail_photo = models.ImageField(upload_to='images/%Y/%m/%d')
    intro = models.CharField(max_length=500)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Opublikowany')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.published.year, self.published.strftime('%m'),
                                                 self.published.strftime('%d'), self.slug])

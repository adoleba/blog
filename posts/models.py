from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
from django.db import models
from django.urls import reverse
from django.utils import timezone

from categories.models import Category
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique_for_date='published')
    sub_title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, related_name='posts')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    main_photo = CloudinaryField('Main photo', null=True)
    thumbnail_photo = CloudinaryField('Thumbnail photo', null=True)
    intro = models.CharField(max_length=500)
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.published.year, self.published.strftime('%m'),
                                                 self.published.strftime('%d'), self.slug])


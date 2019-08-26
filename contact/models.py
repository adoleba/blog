from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class ContactPage(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Contact Page, updated: " + str(self.updated.strftime("%d/%m/%Y"))

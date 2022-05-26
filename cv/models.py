from django.db import models

from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Cv(models.Model):
    title = models.TextField(max_length=40)
    body = RichTextField()

    def __str__(self):
        return self.title

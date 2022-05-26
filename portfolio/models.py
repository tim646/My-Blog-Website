from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=200, blank=True)
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        default='temurbek',


    )

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('portfolio')

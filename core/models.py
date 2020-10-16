from hashlib import md5

from django.contrib.auth.models import User
from django.db import models

import random
import string

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver




class UrlShortcut(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    link = models.URLField(unique=True)
    short = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):

        if not self.id:
            self.short = md5(self.link.encode()).hexdigest()[:10]
        return super().save(*args, **kwargs)

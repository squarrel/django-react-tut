from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)

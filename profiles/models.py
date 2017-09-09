from django.db import models

from __future__ import unicode_literals
# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

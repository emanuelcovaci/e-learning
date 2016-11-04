from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Domain(models.Model):
    name = models.CharField(null=True, max_length=20)
    path_banner = models.CharField(null=True, max_length=500)

    def __unicode__(self):
        return self.name

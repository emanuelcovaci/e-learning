from __future__ import unicode_literals

from django.db import models


# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" % (instance.name, filename)

class Domain(models.Model):
    name = models.CharField(null=True, max_length=20)
    image = models.ImageField(upload_to=upload_location,
                               null=True, blank=True)

    def __unicode__(self):
        return self.name

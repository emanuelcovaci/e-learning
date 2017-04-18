from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


def upload_location(instance, filename):
    return "%s/%s" % (instance.user, filename)


class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    profile_image = models.ImageField(upload_to=upload_location,
                                      null=True, blank=True)

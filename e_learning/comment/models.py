from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from lesson.models import Lesson


# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User, related_name='author',
                               null=True, blank=True)
    lesson = models.ForeignKey(Lesson, null=True)
    content = models.CharField(null=True, max_length=1000)
    date = models.DateTimeField(auto_now_add=True,editable=False,
                                         null=True)

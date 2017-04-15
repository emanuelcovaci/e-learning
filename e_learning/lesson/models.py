# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from domain.models import Domain


def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)


class Lesson(models.Model):
    title = models.CharField(null=True, max_length=30)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_location,
                               null=True, blank=True)
    image3 = models.ImageField(upload_to=upload_location,
                               null=True, blank=True)
    description = models.CharField('Task description',
                                   null=True, max_length=500)
    slug = models.SlugField(default=uuid.uuid1, unique=True)
    author = models.ForeignKey(User, related_name='posts',
                               null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False,
                                         null=True)
    domain = models.ForeignKey(Domain, null=True)

    title_paragraf_1 = models.CharField(null=True, max_length=30)
    paragraf_1 = models.CharField(null=True, max_length=5000)

    title_paragraf_2 = models.CharField(null=True, max_length=30)
    paragraf_2 = models.CharField(null=True, max_length=5000)

    def get_absolute_url(self):
        return reverse('lesson', args=[self.slug])

    class Meta:
        get_latest_by = 'creation_date'

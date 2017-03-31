from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lesson/(?P<name>.+?)/(?P<slug>[^\.]+)/$', views.lesson, name='lesson'),
]
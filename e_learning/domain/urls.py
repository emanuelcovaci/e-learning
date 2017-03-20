from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'(?P<kind>.+?)/$', views.domain, name='domain'),



]

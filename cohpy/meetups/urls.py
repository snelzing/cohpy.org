# from django.conf.urls import patterns, url
from django.urls import re_path

from meetups import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]

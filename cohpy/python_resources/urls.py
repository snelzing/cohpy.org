# from django.conf.urls import patterns, url

from python_resources import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]

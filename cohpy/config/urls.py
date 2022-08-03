# I think this is a django 1.8 thing and may need gotten rid of but really not sure
# from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.urls import re_path, include

from meetups import views


urlpatterns = [
    re_path(r'^$', views.home_page, name='home'),
    re_path(r'^meetups/', include('meetups.urls')),
    re_path(r'^resources/', include('python_resources.urls')),
    re_path(r'^admin/', admin.site.urls),
]

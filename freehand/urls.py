"""
Freehand URL Configuration
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pages.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^shuttle/', include('shuttle.urls')),
]

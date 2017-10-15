"""
URL Configuration for Hire App
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^drivers/', include('drivers.urls')),
]

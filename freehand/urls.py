"""freehand URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pages.urls')),
    # url(r'^drivers/', include('drivers.urls')),
    # url(r'^cars/', include('cars.urls')),
    # url(r'^shuttle/', include('shuttle.urls')),
]

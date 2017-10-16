from django.conf.urls import url
from . import views

app_name = "drivers"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<id>[0-9]+)/$', views.driver_info, name="driver"),
]

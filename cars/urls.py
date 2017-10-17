from django.conf.urls import url
from . import views

app_name = "cars"

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^(?P<id>[0-9]+)/$', views.car_info, name="info"),
]

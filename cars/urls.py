from django.conf.urls import url
from . import views

app_name = "cars"

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(
    r'^api/car_orders$',
    views.CarOrdersList.as_view(),
    name="car_orders_api"
  ),
  url(r'^(?P<id>[0-9]+)/$', views.car_info, name="info"),
  url(r'^request/car/$', views.car_request, name="request"),
]

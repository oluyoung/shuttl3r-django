from django.conf.urls import url
from . import views

app_name = "shuttle"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<id>[0-9]+)/$', views.select, name="select"),
    url(r'^subscribe/$', views.shuttle_request, name="request")
]

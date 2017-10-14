from django.conf.urls import url
from . import views

app_name = "pages"

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^contact$', views.contact, name="contact"),
  url(r'^apply$', views.apply, name="apply"),
  url(r'^faq$', views.faq, name="faq"),
]

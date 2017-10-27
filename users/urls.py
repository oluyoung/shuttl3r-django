from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = "users"

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/dashboard$', views.dashboard, name="dashboard"),
    url(r'^(?P<id>[0-9]+)/account/$', views.account, name="account"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),    
]

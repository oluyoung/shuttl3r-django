from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = "users"

urlpatterns = [
    url(r'^user/dashboard/$', views.dashboard, name="dashboard"),
    url(r'^user/account/$', views.account, name="account"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^user/delete/$', views.delete_account, name='delete')
]

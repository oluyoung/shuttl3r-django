"""freehand URL Configuration

"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pages.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social'))
    url(r'^hire/', include('hire.urls')),
    # url(r'^cars/', include('cars.urls')),
    # url(r'^shuttle/', include('shuttle.urls')),
]

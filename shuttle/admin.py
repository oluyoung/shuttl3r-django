from django.contrib import admin
from .models import ShuttleBus, ShuttleRoute, RouteStop, ShuttleOrder


# Register your models here.
admin.site.register(ShuttleBus)
admin.site.register(ShuttleRoute)
admin.site.register(RouteStop)
admin.site.register(ShuttleOrder)

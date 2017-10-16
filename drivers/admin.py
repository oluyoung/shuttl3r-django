from django.contrib import admin
from .models import DriverInfo, DriverOrder, Driver_CV

# Register your models here.
admin.site.register(DriverInfo)
admin.site.register(DriverOrder)
admin.site.register(Driver_CV)

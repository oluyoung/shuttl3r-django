from django.shortcuts import render, get_object_or_404
from .models import DriverInfo


# Create your views here.
def index(request):
    drivers = DriverInfo.objects.all()
    return render(request, 'drivers/index.html', {'drivers': drivers})


def driver_info(request, id):
    driver = DriverInfo.objects.get(pk=id)
    return render(request, 'drivers/driver.html', {'driver': driver})

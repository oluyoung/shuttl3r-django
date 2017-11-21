from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import DriverInfo, DriverOrder
from users.models import User


# Create your views here.
def index(request):
    drivers = DriverInfo.objects.all()
    if request.user.is_authenticated:
        user = request.user
        context = {'drivers': drivers, 'user': user}
    else:
        context = {'drivers': drivers}

    return render(request, 'drivers/index.html', context)


def driver_info(request, id):
    driver = get_object_or_404(DriverInfo, pk=id)
    # driver = DriverInfo.objects.get(pk=id)
    return render(request, 'drivers/driver.html', {'driver': driver})


def driver_request(request):
    if request.method == 'POST':
        user_id = request.POST['user']
        if request.POST['is_within_lagos'] == 'true':
            within = True
        else:
            within = False

        DriverOrder.objects.create(
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            is_within_lagos=within,
            pickup_address=request.POST['pickup_address'],
            user=User.objects.get(pk=user_id),
        )

        return HttpResponse('Successful entry')

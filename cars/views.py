from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import CarInfo, CarOrder
from users.models import User


# Create your views here.
def index(request):
    cars = CarInfo.objects.all()
    if request.user.is_authenticated:
        user = request.user
    context = {'cars': cars, 'user': user}
    return render(request, 'cars/index.html', context)


def car_info(request, id):
    car = get_object_or_404(CarInfo, pk=id)
    context = {'car': car}
    return render(request, 'cars/car.html', context)


def car_request(request):
    if request.method == 'POST':
        car_id = request.POST['item_id']
        user_id = request.POST['user']
        if request.POST['is_within_lagos'] == 'true':
            within = True
        else:
            within = False

        CarOrder.objects.create(
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            is_within_lagos=within,
            pickup_address=request.POST['pickup_address'],
            car=CarInfo.objects.get(pk=car_id),
            user=User.objects.get(pk=user_id),
        )

        return HttpResponse('Successful entry')

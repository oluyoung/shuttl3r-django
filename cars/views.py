from django.shortcuts import render
from .models import CarInfo


# Create your views here.
def index(request):
    cars = CarInfo.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'cars/index.html', context)


def car_info(request, id):
    car = CarInfo.objects.get(pk=id)
    context = {
        'car': car
    }

    return render(request, 'cars/car.html', context)

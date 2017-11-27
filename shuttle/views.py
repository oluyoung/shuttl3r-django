from django.shortcuts import render
from django.http import HttpResponse
from .models import ShuttleRoute, RouteStop, ShuttleOrder
from users.models import User


# Create your views here.
def index(request):
    routes = ShuttleRoute.objects.all()
    # route_stops = RouteStop.objects.all()
    if request.user.is_authenticated:
        user = request.user
        context = {'routes': routes, 'user': user}
    else:
        context = {'routes': routes}

    return render(request, 'shuttle/index.html', context)


def select(request, id):
    route = ShuttleRoute.objects.get(pk=id)
    route_stops = RouteStop.objects.filter(route=route).order_by('stop_no')
    if request.user.is_authenticated:
        user = request.user
    context = {
        'route': route,
        'stops': route_stops,
        'user': user
    }

    return render(request, 'shuttle/select.html', context)


def shuttle_request(request):
    if request.method == 'POST':
        route_id = request.POST['item_id']
        user_id = request.POST['user']
        morning_stop = request.POST['morning_stop']
        evening_stop = request.POST['evening_stop']

        ShuttleOrder.objects.create(
            subscription=request.POST['subscription'],
            morning_pickup_stop=RouteStop.objects.get(pk=morning_stop),
            morning_pickup_time=request.POST['morning_time'],
            evening_pickup_stop=RouteStop.objects.get(pk=evening_stop),
            evening_pickup_time=request.POST['evening_time'],
            daily_pickup_date=request.POST['start_date'],
            route=ShuttleRoute.objects.get(pk=route_id),
            user=User.objects.get(pk=user_id),
            isRenewing=False,
        )

        route = ShuttleRoute.objects.get(pk=route_id)
        if route.seats_available > 0:
            route.seats_available -= 1
        else:
            route.is_available = False
        route.save()

        # check return value of .create
        # alert user if already subscribed to a route

        return HttpResponse('Successful entry')

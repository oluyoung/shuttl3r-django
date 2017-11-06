from django.shortcuts import render
from django.http import HttpResponse
from .models import ShuttleRoute, RouteStop, ShuttleOrder
from users.models import User


# Create your views here.
def index(request):
    routes = ShuttleRoute.objects.all()
    # route_stops = RouteStop.objects.all()
    return render(request, 'shuttle/index.html', {'routes': routes})


def select(request, id):
    route = ShuttleRoute.objects.get(pk=id)
    route_stops = RouteStop.objects.filter(route=route).order_by('stop_no')
    if request.user.is_authenticated:
        user = request.user
    context = {'route': route, 'stops': route_stops, 'user': user}
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
            route=ShuttleRoute.objects.get(pk=route_id),
            user=User.objects.get(pk=user_id),
            isRenewing=False,
        )

        # reduce seats available from Route
          # check return alue of .create
          # alert user if already subscribed to a route

        return HttpResponse('Successful entry')

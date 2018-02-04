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
        has_ongoing = False

        if ShuttleOrder.objects.filter(user=user).exclude(status='Completed'):
            has_ongoing = True

        context = {'routes': routes, 'user': user, 'has_ongoing': has_ongoing}
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
        route = ShuttleRoute.objects.get(pk=request.POST['item_id'])
        # user = User.objects.get(pk=request.POST['user'])
        subscription = request.POST['subscription']
        morning_stop = request.POST['morning_stop']
        evening_stop = request.POST['evening_stop']

        if request.user.is_authenticated:
            ShuttleOrder.objects.create(
                subscription=subscription,
                morning_pickup_stop=RouteStop.objects.get(pk=morning_stop),
                morning_pickup_time=request.POST['morning_time'],
                evening_pickup_stop=RouteStop.objects.get(pk=evening_stop),
                evening_pickup_time=request.POST['evening_time'],
                # daily_pickup_date=daily_pickup_date,
                route=route,
                user=request.user,
                isRenewing=False,
            )

            if route.seats_available > 0:
                route.seats_available -= 1
            else:
                route.is_available = False
            route.save()

            # check return value of .create
            # alert user if already subscribed to a route

            return HttpResponse('Successful entry')

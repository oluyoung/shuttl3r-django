from django.db import models
from users.models import User


# Create your models here.
class ShuttleBus(models.Model):
    """
    Description: Model describing a Bus
    """
    BUS_CHOICES = (
        ('Mini Bus', 'Mini Bus'),
        ('Coaster Bus', 'Coaster Bus'),
    )
    bus_type = models.CharField(max_length=15, choices=BUS_CHOICES)
    license = models.CharField(max_length=10)
    seat_num = models.IntegerField()

    class Meta:
        verbose_name = "ShuttleBus"
        verbose_name_plural = "ShuttleBuses"

    def __str__(self):
        return "%s with %s seats" % (self.bus_type, self.seat_num)


class ShuttleRoute(models.Model):
    """
    Description: Model describing a Route
    """
    bus = models.ForeignKey(ShuttleBus, on_delete=models.CASCADE)
    seats_available = models.IntegerField() # get from bus.seat_num
    route_name = models.CharField(max_length=255)
    startpoint = models.CharField(max_length=255)
    endpoint = models.CharField(max_length=255)
    # one_way_price_per_day = models.IntegerField()
    # one_way_price_per_week = models.IntegerField()
    # one_way_price_per_month = models.IntegerField()
    daily_price = models.IntegerField()
    weekly_price = models.IntegerField()
    monthly_price = models.IntegerField()
    is_available = models.BooleanField()
    
    class Meta:
        verbose_name = "ShuttleRoute"    
        verbose_name_plural = "ShuttleRoutes"

    def __str__(self):
        return "From: %s, To: %s, Time: %s - %s" % (self.startpoint, self.endpoint, self.go_time, self.return_time)


class RouteStop(models.Model):
    """
    Description: Model describing a Route's stop
    """
    route = models.ForeignKey(ShuttleRoute)
    stop_slug = models.SlugField()
    stop_location = models.CharField(max_length=255)

    class Meta:
        verbose_name = "RouteStop"
        verbose_name_plural = "RouteStops"

    def __str__(self):
        return "%s on Route: %s" % (self.stop_location, self.route.route_name)


class ShuttleOrder(models.Model):
    """
    Description: Model describing a shuttle order/subscription
    """
    route = models.ForeignKey(ShuttleRoute, on_delete=models.CASCADE, related_name='route')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    # if is one way show 
    # is_one_way = models.isBooleanField()
    # ONE_WAY_CHOICES = (('Morning', 'Morning'),('Evening', 'Evening')) # morning or evening
    # one_way_way = models.ChoiceField(choices='ONE_WAY_CHOICES', null=True, blank=True)
    SUBSCRIPTION_CHOICES = (('Daily', 'Daily'),('Weekly', 'Weekly'),('Monthly', 'Monthly'))
    subscription = models.CharField(max_length=10, choices=SUBSCRIPTION_CHOICES)
    renew = models.BooleanField()
    TIME_CHOICES = (
        ('5:00','5:00'),('5:30','5:30'),('6:00','6:00'),('6:30','6:30'),('7:00','7:00'),
        ('7:30','7:30'),('8:00','8:00'),('8:30','8:30'),('9:00','9:00'),('9:30','9:30')
    )
    morning_time = models.TimeField(choices=TIME_CHOICES)
    evening_time = models.TimeField(choices=TIME_CHOICES)
    morning_pickup_stop = models.ForeignKey(RouteStop, on_delete=models.CASCADE, related_name='morning_pickup_stop')
    morning_dropoff_stop = models.ForeignKey(RouteStop, on_delete=models.CASCADE, related_name='morning_dropoff_stop')
    evening_pickup_stop = models.ForeignKey(RouteStop, on_delete=models.CASCADE, related_name='evening_pickup_stop')
    evening_dropoff_stop = models.ForeignKey(RouteStop, on_delete=models.CASCADE, related_name='evening_dropoff_stop')
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ShuttleOrder"
        verbose_name_plural = "ShuttleOrders"

    def __str__(self):
        morning = "Morning: %s on %s route @ %s from %s." % (self.user.get_full_name, self.route.route_name, self.morning_time, self.evening_time)
        evening = "Evening: %s on %s route @ %s from %s." % (self.user.get_full_name, self.route.route_name, self.morning_time, self.evening_time)
        return morning + evening

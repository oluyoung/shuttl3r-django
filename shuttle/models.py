from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class ShuttleBus(models.Model):
    """
    Description: Model describing a Bus
    """
    BUS_CHOICES = (
        ('Mini Bus', 'Mini Bus'),
        ('Coaster Bus', 'Coaster Bus'),
    )
    bus_type = models.CharField(_('Bus Type'), max_length=15, choices=BUS_CHOICES)
    license = models.CharField(_('License Plate'), max_length=10)

    class Meta:
        verbose_name = "ShuttleBus"
        verbose_name_plural = "ShuttleBuses"

    def __str__(self):
        return "%s: %s" % (self.bus_type, self.license)


class ShuttleRoute(models.Model):
    """
    Description: Model describing a Route
    """
    seats_num = models.IntegerField(_('No. of Seats'))
    # get from bus.seat_num
    seats_available = models.IntegerField(_('No. of Seats Available'), default=seats_num)
    route_name = models.CharField(_('Route Title'), max_length=255)
    startpoint = models.CharField(_('Route Start Location'), max_length=255)
    morning_start_time = models.TimeField(_('Route Morning Start Time'))
    start_latitude = models.CharField(_('Route Start Location Latitude'), max_length=25, null=True, blank=True)
    start_longitude = models.CharField(_('Route Start Location Longitude'), max_length=25, null=True, blank=True)
    endpoint = models.CharField(_('Route End Location'), max_length=255)
    evening_start_time = models.TimeField(_('Route Evening Start Time')) # time that return journey begins
    end_latitude = models.CharField(_('Route End Location Latitude'), max_length=25, null=True, blank=True)
    end_longitude = models.CharField(_('Route End Location Longitude'), max_length=25, null=True, blank=True)
    # eta = models.TimeField() # to get there
    # one_way_price_per_day = models.IntegerField()
    # one_way_price_per_week = models.IntegerField()
    # one_way_price_per_month = models.IntegerField()
    daily_pickup_date = models.DateTimeField(_('Daily Pickup Date'), null=True, blank=True)
    daily_price = models.FloatField(_('Route Daily Price'))
    weekly_price = models.FloatField(_('Route Weekly Price'))
    monthly_price = models.FloatField(_('Route Monthly Price'))
    is_available = models.BooleanField(_('Is Route Still Available for Subscribers?'), default=True)

    class Meta:
        verbose_name = "ShuttleRoute"    
        verbose_name_plural = "ShuttleRoutes"

    def get_first_stop(self):
        return self.routestop_set.all().order_by('stop_no')[0]

    def get_last_stop(self):
        count = self.routestop_set.all().order_by('stop_no').count()
        return self.routestop_set.all().order_by('stop_no')[count-1]

    def get_mid_stops(self):
        count = self.routestop_set.all().order_by('stop_no').count()
        return self.routestop_set.all().order_by('stop_no')[1:count-1]

    def get_all_stops(self):
        return self.routestop_set.all().order_by('stop_no')        

    def __str__(self):
        return "From: %s, To: %s, Time: %s/%s" % (self.startpoint, self.endpoint, self.morning_start_time, self.evening_start_time)


class RouteStop(models.Model):
    """
    Description: Model describing a Route's stop
    """
    route = models.ForeignKey(ShuttleRoute)
    stop_no = models.IntegerField() # gets stop order no from 1
    stop_location = models.CharField(max_length=255)
    # stop_long_name = models.CharField(max_length=255)
    # to be included for G Map API
    # short_name = models.CharField(max_length=255)
    # long_name = models.CharField(max_length=255)

    morning_start_time = models.TimeField(null=True, blank=True)
    # time that return journey begins
    evening_start_time = models.TimeField(null=True, blank=True)
    # STOP_TYPE_CHOICES = (
    #     ('Morning', 'Morning'),
    #     ('Evening', 'Evening'),
    #     ('Both', 'Both')
    # )
    # stop_type = models.CharField(max_length=10, choices=STOP_TYPE_CHOICES)
    latitude = models.CharField(max_length=25, null=True, blank=True)
    longitude = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        verbose_name = "RouteStop"
        verbose_name_plural = "RouteStops"

    def __str__(self):
        return "Stop %d: %s on Route: %s" % (self.stop_no, self.stop_location, self.route.route_name)


class ShuttleOrder(models.Model):
    """
    Description: Model describing a shuttle order/subscription
    """
    order_date = models.DateTimeField(auto_now_add=True)
    route = models.ForeignKey(ShuttleRoute, related_name='route')
    user = models.ForeignKey(User, related_name='user')
    # if is one way show 
    # is_one_way = models.isBooleanField()
    # ONE_WAY_CHOICES = (('Morning', 'Morning'),('Evening', 'Evening')) # morning or evening
    # one_way_way = models.ChoiceField(choices='ONE_WAY_CHOICES', null=True, blank=True)
    SUBSCRIPTION_CHOICES = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly')
    )
    subscription = models.CharField(max_length=10, choices=SUBSCRIPTION_CHOICES)
    TIME_CHOICES = (
        ('5:00','5:00'),('5:30','5:30'),('6:00','6:00'),('6:30','6:30'),('7:00','7:00'),
        ('7:30','7:30'),('8:00','8:00'),('8:30','8:30'),
    )
     #,('9:00','9:00'),('9:30','9:30') late night shuttle
    morning_pickup_time = models.TimeField(_('User\'s Morning Pickup Time'), choices=TIME_CHOICES)
    evening_pickup_time = models.TimeField(_('User\'s Evening Pickup Time'), choices=TIME_CHOICES)
    morning_pickup_stop = models.ForeignKey(RouteStop, related_name='morning_pickup_stop')
    evening_pickup_stop = models.ForeignKey(RouteStop, related_name='evening_pickup_stop')
    isRenewing = models.BooleanField(_('Is User\'s Subscription Renewed?'))
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
        ('Not Started', 'Not Started'),
        ('Cancelled', 'Cancelled')
    )
    # status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "ShuttleOrder"
        verbose_name_plural = "ShuttleOrders"

    def __str__(self):
        morning = "%s: Morning: %s route @ %s from %s." % (self.user.get_full_name(), self.route.route_name, self.morning_pickup_time, self.morning_pickup_stop.stop_location)
        evening = "Evening: %s route @ %s from %s." % (self.route.route_name, self.evening_pickup_time, self.evening_pickup_stop.stop_location)
        return morning, evening

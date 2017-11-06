from django.db import models
from users.models import User


# Create your models here.
class CarInfo(models.Model):
    """
    Description: Stores infromation for each car in store
    """
    VEHICLE_TYPE = (
        ('Space Bus', 'Space Bus'),
        ('SUV', 'SUV'),
        ('Saloon Car', 'Saloon Car'),
        ('Coaster Bus', 'Coaster Bus'),
        ('Mini Bus', 'Mini Bus'),
    )
    vehicle_type = models.CharField(max_length=15, choices=VEHICLE_TYPE)
    make = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=20)
    # image = models.FileField(upload_to='uploads/cars')
    image_url = models.URLField(null=True, blank=True)
    # admin
    license_plate = models.CharField(max_length=15)
    luxury = models.BooleanField()
    # admin
    available_for_use = models.BooleanField()
    # papers
    isAvailable = models.BooleanField()
    nextAvailability = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'CarInfo'
        verbose_name_plural = 'CarInfos'

    def __str__(self):
        return ('%s: %s') % (self.vehicle_type, self.license_plate)


class CarOrder(models.Model):
    """
    Description: Stores information for each car's order
    """
    # use timestamp to create charts in admin dash with API
    order_date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_within_lagos = models.BooleanField()
    pickup_address = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'CarOrder'
        verbose_name_plural = 'CarOrders'

    def __str__(self):
        return "%s: %s" % (self.order_date, self.user.get_full_name())

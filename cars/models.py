from django.db import models
from users.models import User
from django.db.models.signals import pre_save, post_save
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.utils.crypto import get_random_string


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

    def get_full_name(self):
        return ('%s %s') % (self.make.capitalize(), self.name.capitalize())

    def __str__(self):
        return ('%s: %s') % (self.vehicle_type, self.license_plate)


class CarOrder(models.Model):
    """
    Description: Stores information for each car's order
    """
    # use timestamp to create charts in admin dash with API
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    start_date = models.DateField()
    end_date = models.DateField()
    is_within_lagos = models.BooleanField()
    pickup_address = models.CharField(max_length=255)
    CATEGORY_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    # time not needed
    pickup_time = models.DateTimeField()
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
        ('Not Started', 'Not Started'),
        ('Cancelled', 'Cancelled')
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Not Started'
    )
    reservation_number = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True
    )

    class Meta:
        verbose_name = 'CarOrder'
        verbose_name_plural = 'CarOrders'

    def __str__(self):
        return "%s: %s" % (self.order_date, self.user.get_full_name())


@receiver(pre_save, sender=CarOrder)
def generate_res_num(sender, instance, *args, **kwargs):
    instance.reservation_number = (
        "%s%s%d%s" %
        (
            instance.user.first_name[0].upper(),
            instance.user.last_name[0].upper(),
            instance.id,
            get_random_string(length=8)
        )
    )


@receiver(post_save, sender=CarOrder)
def send_order_email(sender, instance, *args, **kwargs):
    message = render_to_string('user/reserverd_order.html', {
        'user': instance.user,
    })
    instance.user.email_user(
        subject='DriveHub Driver Reservation',
        message='',
        from_email='freehand@sendgrid.net',
        to_email=[instance.user.email],
        fail_silently=False,
        html_message=message)

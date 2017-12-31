from django.db import models
from users.models import User


# Create your models here.
class DriverInfo(models.Model):
    first_name = models.CharField(max_length=255)
    mid_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    # image = models.FileField(upload_to='uploads/drivers')
    image_url = models.URLField(null=True, blank=True)
    home_address = models.CharField(max_length=255)
    phone_num1 = models.CharField(max_length=11, null=False)
    phone_num2 = models.CharField(max_length=11, null=True, blank=True)
    # upvotes/downvotes
    # class_a - long distance, short distance, extended
    # class_b - short distance (i.e. within state)
    # class_c - weekend
    CATEGORY_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    available_for_use = models.BooleanField()
    # should be manipulated by user or gotten from last order date
    isAvailable = models.BooleanField()
    # get this from last order end date
    nextAvailability = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'DriverInfo'
        verbose_name_plural = 'DriverInfos'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name.
        '''
        full_name = '%s, %s' % (self.last_name.capitalize(), self.first_name.capitalize())
        return full_name.strip()

    def __str__(self):
        return "%s: %s" % (self.id, self.get_full_name())


class DriverOrder(models.Model):
    """
    Description: Keeps records of each order
    """
    order_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_within_lagos = models.BooleanField()
    pickup_address = models.CharField(max_length=255)
    # time not needed
    pickup_time = models.DateTimeField()
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
        ('Not Started', 'Not Started'),
        ('Cancelled', 'Cancelled')
    )
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Not Started')
    CATEGORY_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'DriverOrder'
        verbose_name_plural = 'DriverOrders'

    def __str__(self):
        return "%s: %s" % (self.order_date, self.user.get_full_name())


class Driver_CV(models.Model):
    driver = models.ForeignKey(DriverInfo, on_delete=models.CASCADE)
    how_many_years_driving_professionally = models.IntegerField()
    last_employer_name = models.CharField(max_length=255)
    last_employer_address = models.CharField(max_length=255)
    last_employer_number = models.CharField(max_length=11)
    reason_for_leaving = models.CharField(max_length=255)
    license_id = models.CharField(max_length=15)
    license_exp_date = models.DateField()
    medical_conditions = models.TextField(default='Nil')
    referee1 = models.CharField(max_length=255, null=False)
    home_office_num1 = models.CharField(max_length=11, null=False)
    home_office_addr1 = models.CharField(max_length=255, null=False)
    referee2 = models.CharField(max_length=255, null=True, blank=True)
    home_office_num2 = models.CharField(max_length=11, null=True, blank=True)
    home_office_addr2 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Driver_CV'
        verbose_name_plural = 'Driver_CVs'

    def __str__(self):
        return "%s" % (self.get_full_name)

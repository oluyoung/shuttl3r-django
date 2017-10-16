from django.db import models


# Create your models here.
class DriverInfo(models.Model):
    first_name = models.CharField(max_length=255)
    mid_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    image = models.FileField(upload_to='uploads/drivers')
    home_address = models.CharField(max_length=255)
    phone_num1 = models.CharField(max_length=11, null=False)
    phone_num2 = models.CharField(max_length=11, null=True)
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
    # should be manipulated by user or gotten from last order date
    isAvailabile = models.BooleanField()
    # get this from last order end date
    nextAvailibility = models.DateField()

    class Meta:
        verbose_name = 'DriverInfo'
        verbose_name_plural = 'DriverInfos'

    def __str__(self):
        return "%s: %s, %s" % (self.id, self.last_name, self.first_name)


class DriverOrder(models.Model):
    """
    Description: Model Description
    """
    timestamp = models.DateField(auto_now_add=True)
    requester_name = models.CharField(max_length=255)
    requester_addr = models.CharField(max_length=255)
    requester_phone = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_within_lagos = models.BooleanField()
    pickup_address = models.CharField(max_length=255)
    # pickup_time = models.DateTimeField() # time not needed
    driver = models.ForeignKey(DriverInfo, on_delete=models.CASCADE, related_name='driver')

    class Meta:
        verbose_name = 'DriverOrder'
        verbose_name_plural = 'DriverOrders'

    def __str__(self):
        pass


class Driver_CV(models.Model):
    driver = models.ForeignKey(DriverInfo, on_delete=models.CASCADE)
    how_many_years_driving_professionally = models.IntegerField()
    last_employer_name = models.CharField(max_length=255)
    last_employer_address = models.CharField(max_length=255)
    last_employer_number = models.CharField(max_length=255)
    reason_for_leaving = models.CharField(max_length=255)
    license_id = models.CharField(max_length=15)
    license_exp_date = models.DateField()
    medical_conditions = models.TextField()
    referee1 = models.CharField(max_length=255, null=False)
    home_office_num1 = models.CharField(max_length=255, null=False)
    home_office_addr1 = models.CharField(max_length=255, null=False)
    referee2 = models.CharField(max_length=255, null=True)
    home_office_num2 = models.CharField(max_length=255, null=True)
    home_office_addr2 = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = 'Driver_CV'
        verbose_name_plural = 'Driver_CVs'

    def __str__(self):
        pass

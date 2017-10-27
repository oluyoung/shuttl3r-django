import datetime
from django.test import TestCase
from django.utils import timezone


# Create your tests here.


# successful order registered
# edit order successful
# cancel order success
# subscription renewal possible
# renewal status
# seats reduce as orders come in
# no seats after bus is filled
# have to be able to spot that when one-way gets off then a space is available for evening
# have to be able to say that if someone changes routes then a space is available
# has to detect subscription date ends and starts
# has to detect is subscription per day
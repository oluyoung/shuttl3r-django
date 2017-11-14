from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('First Name'), max_length=35)
    last_name = models.CharField(_('Last Name'), max_length=35)
    email = models.EmailField(_('Email Address'), unique=True)
    phone_num = models.CharField(_('Phone Number'), max_length=11)
    default_pickup_addr = models.CharField(_('Default Pickup Address'), max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_num']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def get_id(self):
        return self.id

    def get_absolute_url(self):
        return "/users/%s/dashboard" % urlquote(self.email)

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s, %s' % (self.last_name.upper(), self.first_name.lower())
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # def get_most_recent_driver_orders:


    def __str__(self):
        return "%d: %s" % (self.id, self.get_full_name())

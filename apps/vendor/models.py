from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings


class Vendor(models.Model):
    name = models.CharField(
        _('Name'), max_length=100,
        unique=True,
        help_text=_('Unique name going to decide the slug'))
    email = models.EmailField(
        _('Email'),
        max_length=255, help_text=_('Email Address'))
    mobile = models.CharField(
        _('Mobile Number'), blank=True,
        max_length=20, help_text=_('Mobile Number'))
    is_active = models.BooleanField(
        default=False, help_text='Designates whether a vendor is active or not')

    def __str__(self):
        return self.name


class VendorHierarchy(models.Model):
    vendee = models.ForeignKey(Vendor)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_active = models.BooleanField(
        default=False, help_text='Designates whether a vendor hierarchy is active or not')

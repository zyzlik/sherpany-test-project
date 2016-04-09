from django.db import models
from django.utils.translation import ugettext_lazy as _


class Location(models.Model):
    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_('latitude'))
    lon = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_('longitude'))
    address = models.CharField(verbose_name=_('address'), max_length=50)

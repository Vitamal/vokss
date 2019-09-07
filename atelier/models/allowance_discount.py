from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class AllowanceDiscount(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    coefficient = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Coefficient'))
    label = models.CharField(max_length=255, verbose_name=_('Group'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('atelier:allowance_discount_detail', args=[str(self.id)])

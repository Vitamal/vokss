from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=264, verbose_name=_('Name'))
    minimal_style = models.ForeignKey('atelier.MinimalStyle', on_delete=models.CASCADE,
                                      verbose_name=_('Minimal Style'))
    base_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Base Price'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('atelier:product_detail', args=[str(self.id)])
    
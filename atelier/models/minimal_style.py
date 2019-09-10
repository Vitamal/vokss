from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class MinimalStyle(models.Model):
    name = models.TextField(max_length=264, verbose_name=_('Name'))
    group = models.CharField(max_length=264, verbose_name=_('Product group'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['group']

    def get_absolute_url(self):
        return reverse('atelier:minimal_style_detail', args=[str(self.id)])

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Fabric(models.Model):
    GROUP0 = 'GR0'
    GROUP1 = 'GR1'
    GROUP2 = 'GR2'
    GROUP3 = 'GR3'
    GROUP4 = 'GR4'
    FABRIC_GROUPS = [
        (GROUP0, 'Група 0'),
        (GROUP1, 'Група І'),
        (GROUP2, 'Група ІІ'),
        (GROUP3, 'Група ІІІ'),
        (GROUP4, 'Група ІV'),
    ]
    name = models.CharField(max_length=264, verbose_name=_('Name'))
    group = models.CharField(max_length=3,choices=FABRIC_GROUPS, default=GROUP2, verbose_name=_('Group'))
    complexity_factor = models.DecimalField(default=1, max_digits=5, decimal_places=2,
                                            verbose_name=_('Complexity Factor'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['group']

    def get_absolute_url(self):
        return reverse('atelier:fabric_detail', args=[str(self.id)])

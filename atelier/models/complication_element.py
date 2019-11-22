from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from atelier.models import AbstractBaseModel


class ComplicationElement(AbstractBaseModel):
    name = models.CharField(
        max_length=264,
        verbose_name=_('name')
    )
    base_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('base price')
    )
    complexity = models.DecimalField(
        default=1, max_digits=3,
        decimal_places=2,
        verbose_name=_('complexity')
    )
    group = models.CharField(
        default='4',
        max_length=255,
        verbose_name=_("group name")
    )

    def __str__(self):
        """
        to display an object in the Django admin site
        and as the value inserted into a template when it displays an object
        """
        return '{} {}'.format(self.group, self.name)

    class Meta:
        ordering = ['group']

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('atelier:complication_element_detail', args=[str(self.id)])

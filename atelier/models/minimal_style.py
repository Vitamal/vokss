from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from atelier.models import AbstractBaseModel


class MinimalStyleQueryset(models.QuerySet):
    def filter_by_name(self, name):
        return self.filter(name=name)


class MinimalStyle(AbstractBaseModel):
    name = models.TextField(max_length=264, verbose_name=_('name'))
    group = models.CharField(max_length=264, verbose_name=_('product group'))

    def __str__(self):
        """
                to display an object in the Django admin site
                and as the value inserted into a template when it displays an object
                """
        return self.name

    class Meta:
        ordering = ['group']

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('atelier:minimal_style_detail', args=[str(self.id)])

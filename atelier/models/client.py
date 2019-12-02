from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from atelier.models import Atelier
from atelier.models.abstract_base import AbstractBaseModel


class Client(AbstractBaseModel):
    first_name = models.CharField(
        max_length=30,
        verbose_name=_('first Name')
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name=_('second Name')
    )
    tel_number = models.CharField(
        max_length=30,
        blank=True,
        verbose_name=_('tel. number')
    )
    place = models.CharField(
        max_length=30,
        verbose_name=_('place')
    )

    atelier = models.ForeignKey(
        Atelier,
        on_delete=models.CASCADE,
        verbose_name=_('atelier'),
        # null=True,
    )

    def __str__(self):
        """
        to display an object in the Django admin site
        and as the value inserted into a template when it displays an object
        """
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('atelier:client_detail', args=[str(self.id)])

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from atelier.models.abstract_base import AbstractBaseModel


class Atelier(AbstractBaseModel):
    name = models.CharField(
        max_length=150,
        verbose_name=_('name')
    )

    def __str__(self):
        """
        to display an object in the Django admin site
        and as the value inserted into a template when it displays an object
        """
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('atelier:atelier_detail', args=[str(self.id)])

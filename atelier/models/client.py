from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=_('first Name'))
    last_name = models.CharField(max_length=30, verbose_name=_('surname'))
    tel_number = models.CharField(max_length=30, blank=True, verbose_name=_('tel. number'))
    place = models.CharField(max_length=30, verbose_name=_('place'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']


    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('atelier:client_detail', args=[str(self.id)])

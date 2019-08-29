from django.db import models
from django.urls import reverse


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tel_number = models.CharField(max_length=30, blank=True, )
    place = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']


    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('atelier:client_detail', args=[str(self.id)])

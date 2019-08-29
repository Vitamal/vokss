from django.db import models
from django.urls import reverse


class ComplicationElement(models.Model):
    name = models.CharField(max_length=264)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    complexity = models.DecimalField(default=1, max_digits=3,decimal_places=2)
    group = models.CharField(default='4', max_length=255)


    def __str__(self):
        return '{} {}'.format(self.group, self.name)

    class Meta:
        ordering = ['group']

    def get_absolute_url(self):
        return reverse('atelier:complication_element_detail', args=[str(self.id)])

from django.db import models
from django.urls import reverse


class Fabric(models.Model):
    name = models.CharField(max_length=264)
    group = models.ForeignKey('atelier.FabricComplexityGroup', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('atelier:fabric_detail', args=[str(self.id)])

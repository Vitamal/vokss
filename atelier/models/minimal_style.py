from django.db import models
from django.urls import reverse


class MinimalStyle(models.Model):
    name = models.CharField(max_length=264)
    group = models.CharField(max_length=264)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['group']

    def get_absolute_url(self):
        return reverse('atelier:fabric_detail', args=[str(self.id)])

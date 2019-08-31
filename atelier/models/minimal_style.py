from django.db import models
from django.urls import reverse


class MinimalStyle(models.Model):
    name = models.TextField(max_length=264, verbose_name="Опис")
    group = models.CharField(max_length=264, verbose_name="Група виробів")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['group']

    def get_absolute_url(self):
        return reverse('atelier:minimal_style_detail', args=[str(self.id)])

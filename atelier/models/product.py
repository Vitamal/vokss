from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=264)
    minimal_style = models.ForeignKey('atelier.Fabric', on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)1

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('atelier:product_detail', args=[str(self.id)])

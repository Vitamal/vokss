from django.db import models
from django.urls import reverse


class Product(models.Model):
    DEFAULT_MINIMAL_STYLE_ID = 1
    name = models.CharField(max_length=264)
    minimal_style = models.ForeignKey('atelier.Fabric', on_delete=models.CASCADE, default=DEFAULT_MINIMAL_STYLE_ID)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('atelier:product_detail', args=[str(self.id)])

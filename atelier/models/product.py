from django.db import models
from django.urls import reverse


class Product(models.Model):
    DEFAULT_MINIMAL_STYLE_ID = 1
    name = models.CharField(max_length=264, verbose_name="Назва")
    minimal_style = models.ForeignKey('atelier.MinimalStyle', on_delete=models.CASCADE, default=DEFAULT_MINIMAL_STYLE_ID,
                                      verbose_name="Мінімальний фасон")
    base_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Базова ціна")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('atelier:product_detail', args=[str(self.id)])

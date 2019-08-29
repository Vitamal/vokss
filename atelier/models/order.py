from django.db import models
import datetime
from django.urls import reverse


class Order(models.Model):
    CATEGORY1 = '1'
    CATEGORY2 = '2'
    PROCESSING_CATEGORY = [
        (CATEGORY1, 'Категорія обробки 1'),
        (CATEGORY2, 'Категорія обробки 2'),
    ]
    client = models.ForeignKey('atelier.Client', on_delete=models.CASCADE)
    product = models.ForeignKey('atelier.Product', on_delete=models.CASCADE)
    fabric = models.ForeignKey('atelier.Fabric', on_delete=models.CASCADE)
    processing_category = models.CharField(max_length=1, choices=PROCESSING_CATEGORY, default=CATEGORY2,)
    complication_elements = models.ManyToManyField('atelier.ComplicationElement', blank=True)
    allowance_discount = models.ManyToManyField('atelier.AllowanceDiscount', blank=True)
    order_date = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ["order_date"]

    def __str__(self):
        return '{} {}'.format(self.client, self.order_date)


    def display_allowance_discount(self):
        """
        Creates a string for the allowance_discount. This is required to display allowance_discount in Admin.
        """
        return ', '.join([allowance_discount.name for allowance_discount in self.allowance_discount.all()[:3]])

    display_allowance_discount.short_description = 'allowance_discount'

    def get_absolute_url(self):
        return reverse('atelier:order_detail', args=[str(self.id)])


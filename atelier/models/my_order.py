from django.db import models
import datetime


class MyOrder(models.Model):
    client = models.ForeignKey('atelier.MyClient', on_delete=models.CASCADE)
    product = models.ForeignKey('atelier.Product', on_delete=models.CASCADE)
    fabric = models.ForeignKey('atelier.Fabric', on_delete=models.CASCADE)
    complication_elements = models.ManyToManyField('atelier.ComplicationElement', blank=True)
    allowance_discount = models.ManyToManyField('atelier.AllowanceDiscount', blank=True)
    element_complexity_group = models.ManyToManyField('atelier.ElementComplexityGroup', blank=True)
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


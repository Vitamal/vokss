from django.db import models
import datetime

class MyOrder(models.Model):
    client = models.ForeignKey('atelier.MyClient', on_delete=models.CASCADE)
    product = models.ForeignKey('atelier.Product', on_delete=models.CASCADE)
    fabric = models.ForeignKey('atelier.Fabric', on_delete=models.CASCADE)
    complication_elements = models.ManyToManyField('atelier.ComplicationElement', blank=True)
    allowance_discount = models.ForeignKey('atelier.AllowanceDiscount', on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ["order_date"]

    def __str__(self):
        return '{} {}'.format(self.client, self.order_date)

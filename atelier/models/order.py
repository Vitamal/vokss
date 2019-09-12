from django.db import models
import datetime
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from atelier.app_utils import order_price_calculation


class Order(models.Model):
    CATEGORY1 = '1'
    CATEGORY2 = '2'
    PROCESSING_CATEGORY = [
        (CATEGORY1, 'Processing category 1'),
        (CATEGORY2, 'Processing category 2'),
    ]
    client = models.ForeignKey('atelier.Client', on_delete=models.CASCADE, verbose_name=_('client'))
    product = models.ForeignKey('atelier.Product', on_delete=models.CASCADE, verbose_name=_('product'))
    fabric = models.ForeignKey('atelier.Fabric', on_delete=models.CASCADE, verbose_name=_('fabric'))
    processing_category = models.CharField(max_length=1, choices=PROCESSING_CATEGORY, default=CATEGORY2,
                                           verbose_name=_('processing category'))
    complication_elements = models.ManyToManyField('atelier.ComplicationElement', blank=True,
                                                   verbose_name=_('complication elements'))
    allowance_discount = models.ManyToManyField('atelier.AllowanceDiscount', blank=True,
                                                verbose_name=_('allowance/discount'))
    order_date = models.DateField(default=datetime.date.today, verbose_name=_('order date'))

    class Meta:
        ordering = ["order_date"]

    def __str__(self):
        return '{} {}'.format(self.client, self.order_date)

    def display_allowance_discount(self):
        """
        Creates a string for the allowance_discount. This is required to display allowance_discount in Admin.
        """
        return ', '.join([allowance_discount.name for allowance_discount in self.allowance_discount.all()[:3]])

    display_allowance_discount.short_description = _('allowance/discount')

    def display_complication_elements(self):
        """
        Creates a string for the complication_elements. This is required to display complication_elements in Admin.
        """
        return ', '.join([complication_elements.name for complication_elements in self.complication_elements.all()[:3]])

    display_complication_elements.short_description = _('complication elements')

    def get_absolute_url(self):
        return reverse('atelier:order_detail', args=[str(self.id)])

    @property
    def order_price(self):

        complication_elements_base_price_list = []
        complication_elements_complexity_list = []
        allowance_discount_coefficient_list = []

        for i in self.complication_elements.all():
            complication_elements_base_price_list.append(i.base_price)

        for j in self.complication_elements.all():
            complication_elements_complexity_list.append(j.complexity)

        for k in self.allowance_discount.all():
            allowance_discount_coefficient_list.append(k.coefficient)

        return order_price_calculation(self.fabric.complexity_factor, self.product.base_price,
                                       complication_elements_base_price_list, complication_elements_complexity_list,
                                       self.processing_category, allowance_discount_coefficient_list)

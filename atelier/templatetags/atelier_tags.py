from django import template
from atelier.app_utils import order_price_calculation
import os

register = template.Library()


@register.simple_tag
def order_price_tag(order):
    complication_elements_base_price_list = []
    complication_elements_complexity_list = []
    allowance_discount_coefficient_list = []

    for i in order.complication_elements.all():
        complication_elements_base_price_list.append(i.base_price)
        complication_elements_complexity_list.append(i.complexity)

    for k in order.allowance_discount.all():
        allowance_discount_coefficient_list.append(k.coefficient)

    return order_price_calculation(order.fabric.complexity_factor, order.product.base_price,
                                   complication_elements_base_price_list, complication_elements_complexity_list,
                                   order.processing_category, allowance_discount_coefficient_list)


@register.simple_tag
def test_css_class(string):
    if os.environ.get('DJANGOENV') == 'test':
        return string
    return None

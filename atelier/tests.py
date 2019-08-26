import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Order


class OrderModelTests(TestCase):

    def test_was_ordered_recently_with_future_order(self):
        """
        was_ordered_recently() returns False for order whose order_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_order = Order(order_date=time)
        self.assertIs(future_order.was_ordered_recently(), False)

def test_was_ordered_recently_with_old_order(self):
    """
    was_ordered_recently() returns False for order whose order_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_order = Order(order_date=time)
    self.assertIs(old_order.was_ordered_recently(), False)

def test_was_ordered_recently_with_recent_order(self):
    """
    was_ordered_recently() returns True for order whose order_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_order = Order(order_date=time)
    self.assertIs(recent_order.was_ordered_recently(), True)

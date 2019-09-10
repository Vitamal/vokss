import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from atelier.models import Order


# class OrderModelTests(TestCase):
#
#     def test_was_ordered_recently_with_future_order(self):
#         """
#         was_ordered_recently() returns False for order whose order_date
#         is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_order = Order(order_date=time)
#         self.assertIs(future_order.was_ordered_recently(), False)

class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

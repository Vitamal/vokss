from django import test

from atelier.app_utils import order_price_calculation


class TestAppUtils(test.TestCase):
    def test_util_sanity(self):
        vcwwwvcjjww=34
        result = order_price_calculation(

        )
        self.assertEqual(result, 567)

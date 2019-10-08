from django import test

from atelier.app_utils import order_price_calculation


class TestAppUtils(test.TestCase):
    def test_util_sanity(self):
        fabric_complexity_factor = 12345.12
        product_base_price = 1234567890.12
        complication_element_base_price = [12345.12, 1.02, 1, 0.55]
        complication_element_complexity = [123.12, 1, 2, 3]
        order_processing_category = 1
        allowance_discount_coefficients = [12345.12, 1.01, 99.99]

        result = order_price_calculation(fabric_complexity_factor, product_base_price, complication_element_base_price,
                            complication_element_complexity, order_processing_category,
                            allowance_discount_coefficients)
        self.assertEqual(result, '227926471619334944.00')

    def test_util_sanity_simple(self):
        fabric_complexity_factor = 1
        product_base_price = 750
        complication_element_base_price = [30, 30, 30, 30, 30, 30, 30, 30, 30]
        complication_element_complexity = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        order_processing_category = 1
        allowance_discount_coefficients = []

        result = order_price_calculation(fabric_complexity_factor, product_base_price, complication_element_base_price,
                            complication_element_complexity, order_processing_category,
                            allowance_discount_coefficients)
        self.assertEqual(result, '1224.00')

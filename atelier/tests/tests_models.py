from django.test import TestCase
from model_mommy import mommy

from atelier.models import Client, AllowanceDiscount, ComplicationElement


class AllowanceDiscountTestModel(TestCase):
    """
    Class to test the model
    AllowanceDiscount
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.allowance_discount = mommy.make(AllowanceDiscount)

    def test_allowence_discount_instance(self):
        allowance_discount = self.allowance_discount
        self.assertTrue(isinstance(allowance_discount, AllowanceDiscount))
        self.assertEqual(allowance_discount.__str__(), allowance_discount.name)

    def test_allowence_discount_fields(self):
        field_name = self.allowance_discount._meta.get_field('name').verbose_name
        field_coefficient = self.allowance_discount._meta.get_field('coefficient').verbose_name
        field_label = self.allowance_discount._meta.get_field('label').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_coefficient, 'coefficient')
        self.assertEquals(field_label, 'group')


class ComplicationElementTestModel(TestCase):
    """
    Class to test the model
    ComplicationElement
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.complication_element = mommy.make(ComplicationElement)
        # self.assertTrue(isinstance(self.complication_element, ComplicationElement))

class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(first_name='Big', last_name='Bob', tel_number='067-200-333-44', place='Stryi')

    def test_first_name_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first Name')

    def test_last_name_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'second Name')

    def test_place_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('place').verbose_name
        self.assertEquals(field_label, 'place')

    def test_tel_number_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('tel_number').verbose_name
        self.assertEquals(field_label, 'tel. number')

    def test_first_name_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)

    def test_tel_number_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('tel_number').max_length
        self.assertEquals(max_length, 30)

    def test_place_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('place').max_length
        self.assertEquals(max_length, 30)

    def test_object_name_is_first_name_last_name(self):
        client = Client.objects.get(id=1)
        expected_object_name = '%s %s' % (client.first_name, client.last_name)
        self.assertEquals(expected_object_name, str(client))

    def test_get_absolute_url(self):
        client = Client.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(client.get_absolute_url(), '/en-us/atelier/client/1/')


class OrderTestModel(TestCase):
    """
        Class to test the module
        Order
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.order = mommy.make('atelier.Order', make_m2m=True)

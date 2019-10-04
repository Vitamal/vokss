from django.test import TestCase
from model_mommy import mommy
from atelier.models import Client, AllowanceDiscount, ComplicationElement, Fabric
from model_mommy.recipe import Recipe

class ClientModelTest(TestCase):
    """
    Class to test the model
    Client
    """
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


class AllowanceDiscountTestModel(TestCase):
    """
    Class to test the model
    AllowanceDiscount by the help of Model Mommy
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.allowance_discount = mommy.make(AllowanceDiscount)

    def test_instance(self):
        self.assertTrue(isinstance(self.allowance_discount, AllowanceDiscount))
        self.assertEqual(self.allowance_discount.__str__(), self.allowance_discount.name)

    def test_fields_verbous_name(self):
        field_name = self.allowance_discount._meta.get_field('name').verbose_name
        field_coefficient = self.allowance_discount._meta.get_field('coefficient').verbose_name
        field_label = self.allowance_discount._meta.get_field('label').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_coefficient, 'coefficient')
        self.assertEquals(field_label, 'group')

    def test_field_arguments(self):
        max_length_name = self.allowance_discount._meta.get_field('name').max_length
        max_length_label = self.allowance_discount._meta.get_field('label').max_length
        max_digits_coefficient = self.allowance_discount._meta.get_field('coefficient').max_digits
        decimal_places_coefficient = self.allowance_discount._meta.get_field('coefficient').decimal_places
        self.assertEquals(max_length_name, 255)
        self.assertEquals(max_length_label, 255)
        self.assertEquals(max_digits_coefficient, 5)
        self.assertEquals(decimal_places_coefficient, 2)

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        self.allowance_discount.id = 1
        self.assertEquals(self.allowance_discount.get_absolute_url(), '/en-us/atelier/allowance_discount/1/')

class FabricTestModel(TestCase):
    """
    Class to test the model
    Fabric (using model mommy Recipe)
    """
    def setUp(self):
        """ Load the recipe 'fabric' from 'atelier/mommy_recipes.py' and create the instances"""
        self.fabric_one = mommy.make_recipe('atelier.fabric')
        # create recip for fabric_wool instance
        self.fabric_wool = Recipe(Fabric, name='Wool', group='GR1', complexity_factor=2,)

    def test_instance(self):
        """True if create instances"""
        self.assertTrue(isinstance(self.fabric_one, Fabric))
        #True if create instance (another instance)
        fabric_wool = self.fabric_wool.make()
        self.assertIsInstance(fabric_wool, Fabric)

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.fabric_one.__str__(), self.fabric_one.name)
        # another instance _str_ checking
        fabric_wool = self.fabric_wool.make()
        self.assertEqual(fabric_wool.__str__(), fabric_wool.name)

    def test_fields_verbous_name(self):
        field_name = self.fabric_one._meta.get_field('name').verbose_name
        field_group = self.fabric_one._meta.get_field('group').verbose_name
        field_complexity_factor = self.fabric_one._meta.get_field('complexity_factor').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_group, 'group')
        self.assertEquals(field_complexity_factor, 'complexity factor')


    def test_field_arguments(self):
        max_length_name = self.fabric_one._meta.get_field('name').max_length
        max_length_group = self.fabric_one._meta.get_field('group').max_length
        max_digits_complexity_factor = self.fabric_one._meta.get_field('complexity_factor').max_digits
        decimal_places_complexity_factor = self.fabric_one._meta.get_field('complexity_factor').decimal_places
        default_complexity_factor = self.fabric_one._meta.get_field('complexity_factor').default
        self.assertEquals(max_length_name, 264)
        self.assertEquals(max_length_group, 3)
        self.assertEquals(max_digits_complexity_factor, 5)
        self.assertEquals(decimal_places_complexity_factor, 2)
        self.assertEquals(default_complexity_factor, 1)

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        self.fabric_one.id = 1
        self.assertEquals(self.fabric_one.get_absolute_url(), '/en-us/atelier/fabric/1/')


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

    def test_instance(self):
        self.assertTrue(isinstance(self.complication_element, ComplicationElement))
        self.assertEqual(self.complication_element.__str__(),
                         '{} {}'.format(self.complication_element.group, self.complication_element.name))


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

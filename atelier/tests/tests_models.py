from django.test import TestCase
from model_mommy import mommy
from atelier.models import Client, AllowanceDiscount, ComplicationElement, Fabric, MinimalStyle, Product, Order


class ClientModelTest(TestCase):
    """
    Class to test the model
    Client
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.client = mommy.make(Client)
        Client.objects.create(first_name='Big', last_name='Bob', tel_number='067-200-333-44', place='Stryi')

    def test_first_name_label(self):
        field_label = self.client._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first Name')

    def test_last_name_label(self):
        field_label = self.client._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'second Name')

    def test_place_label(self):
        field_label = self.client._meta.get_field('place').verbose_name
        self.assertEquals(field_label, 'place')

    def test_tel_number_label(self):
        field_label = self.client._meta.get_field('tel_number').verbose_name
        self.assertEquals(field_label, 'tel. number')

    def test_first_name_max_length(self):
        max_length = self.client._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name_max_length(self):
        max_length = self.client._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)

    def test_tel_number_max_length(self):
        max_length = self.client._meta.get_field('tel_number').max_length
        self.assertEquals(max_length, 30)

    def test_place_max_length(self):
        max_length = self.client._meta.get_field('place').max_length
        self.assertEquals(max_length, 30)

    def test_object_name_is_first_name_last_name(self):
        expected_object_name = '%s %s' % (self.client.first_name, self.client.last_name)
        self.assertEquals(expected_object_name, str(self.client))

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        id = self.client.id
        self.assertEquals(self.client.get_absolute_url(), '/en-us/atelier/client/{}/'.format(id))


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
        id = self.allowance_discount.id
        self.assertEquals(self.allowance_discount.get_absolute_url(),
                          '/en-us/atelier/allowance_discount/{}/'.format(id))


class FabricTestModel(TestCase):
    """
    Class to test the model
    Fabric (using model mommy Recipe)
    """

    def setUp(self):
        """ Load the recipe 'fabric' from 'atelier/mommy_recipes.py' and create the instances"""
        self.fabric_one = mommy.make_recipe('atelier.fabric')
        # create recip for fabric_wool instance
        self.fabric_wool = mommy.make('atelier.Fabric', name='Wool', group='GR1', complexity_factor=2)

    def test_instance(self):
        """True if create instances"""
        self.assertTrue(isinstance(self.fabric_one, Fabric))
        # True if create instance (another instance)
        self.assertIsInstance(self.fabric_wool, Fabric)

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.fabric_one.__str__(), self.fabric_one.name)
        # another instance _str_ checking
        self.assertEqual(self.fabric_wool.__str__(), self.fabric_wool.name)

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
        id = self.fabric_one.id
        self.assertEquals(self.fabric_one.get_absolute_url(), '/en-us/atelier/fabric/{}/'.format(id))


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

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.complication_element.__str__(),
                         '{} {}'.format(self.complication_element.group, self.complication_element.name))

    def test_fields_verbouse_name(self):
        field_name = self.complication_element._meta.get_field('name').verbose_name
        field_group = self.complication_element._meta.get_field('group').verbose_name
        field_base_price = self.complication_element._meta.get_field('base_price').verbose_name
        field_complexity = self.complication_element._meta.get_field('complexity').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_group, 'group name')
        self.assertEquals(field_complexity, 'complexity')
        self.assertEquals(field_base_price, 'base price')

    def test_field_arguments(self):
        max_length_name = self.complication_element._meta.get_field('name').max_length
        max_length_group = self.complication_element._meta.get_field('group').max_length
        default_group = self.complication_element._meta.get_field('group').default
        max_digits_complexity = self.complication_element._meta.get_field('complexity').max_digits
        default_complexity = self.complication_element._meta.get_field('complexity').default
        decimal_places_complexity = self.complication_element._meta.get_field('complexity').decimal_places
        max_digits_base_price = self.complication_element._meta.get_field('base_price').max_digits
        decimal_places_base_price = self.complication_element._meta.get_field('base_price').decimal_places

        self.assertEquals(max_length_name, 264)
        self.assertEquals(max_length_group, 255)
        self.assertEquals(default_group, '4')
        self.assertEquals(max_digits_complexity, 3)
        self.assertEquals(default_complexity, 1)
        self.assertEquals(decimal_places_complexity, 2)
        self.assertEquals(max_digits_base_price, 5)
        self.assertEquals(decimal_places_base_price, 2)

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        id = self.complication_element.id
        self.assertEquals(self.complication_element.get_absolute_url(),
                          '/en-us/atelier/complication_element/{}/'.format(id))


class MinimalStyleTestModel(TestCase):
    """
    Class to test the model
    MinimalStyle
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.minimal_style = mommy.make(MinimalStyle)

    def test_instance(self):
        self.assertTrue(isinstance(self.minimal_style, MinimalStyle))

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.minimal_style.__str__(), self.minimal_style.name)

    def test_fields_verbouse_name(self):
        field_name = self.minimal_style._meta.get_field('name').verbose_name
        field_group = self.minimal_style._meta.get_field('group').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_group, 'product group')

    def test_field_arguments(self):
        max_length_name = self.minimal_style._meta.get_field('name').max_length
        max_length_group = self.minimal_style._meta.get_field('group').max_length

        self.assertEquals(max_length_name, 264)
        self.assertEquals(max_length_group, 264)

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        id = self.minimal_style.id
        self.assertEquals(self.minimal_style.get_absolute_url(), '/en-us/atelier/minimal_style/{}/'.format(id))


class ProductTestModel(TestCase):
    """
    Class to test the model
    Product
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.minimal_style = mommy.make(MinimalStyle)
        self.product = mommy.make(Product, minimal_style=self.minimal_style)

    def test_instance(self):
        self.assertTrue(isinstance(self.product, Product))

    def test_relative_foreign_key(self):
        """
        if Product model foreign key related with MinimalStyle model   :return:true
        """
        self.assertEquals(self.product.minimal_style, self.minimal_style)

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.product.__str__(), self.product.name)

    def test_fields_verbouse_name(self):
        field_name = self.product._meta.get_field('name').verbose_name
        field_minimal_style = self.product._meta.get_field('minimal_style').verbose_name
        field_base_price = self.product._meta.get_field('base_price').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_minimal_style, 'minimal style')
        self.assertEquals(field_base_price, 'base price')

    def test_field_arguments(self):
        max_length_name = self.product._meta.get_field('name').max_length
        max_digits_base_price = self.product._meta.get_field('base_price').max_digits
        decimal_places_base_price = self.product._meta.get_field('base_price').decimal_places
        self.assertEquals(max_length_name, 264)
        self.assertEquals(max_digits_base_price, 10)
        self.assertEquals(decimal_places_base_price, 2)

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        id = self.product.id
        self.assertEquals(self.product.get_absolute_url(), '/en-us/atelier/product/{}/'.format(id))


class OrderTestModel(TestCase):
    """
        Class to test the module
        Order
    """

    def setUp(self):
        """
        Set up all the tests
        """
        complication_element1 = mommy.make(ComplicationElement, name='test1', base_price=10, complexity=2)
        complication_element2 = mommy.make(ComplicationElement, name='test2',base_price=10, complexity=2)
        self.order = mommy.make('atelier.Order', complication_elements=[complication_element1, complication_element2])


    def test_instance(self):
        self.assertTrue(isinstance(self.order, Order))

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.order.__str__(), ('{} {}' .format(self.order.client, self.order.order_date)))
        self.assertEquals(self.order.complication_elements, 2)


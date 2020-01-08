from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from atelier.models import Client, AllowanceDiscount, ComplicationElement, Fabric, MinimalStyle, Product, Order, \
    Atelier, Profile


class ClientModelTest(TestCase):
    """
    Class to test the model
    Client
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.atelier = mommy.make(Atelier)
        self.client = mommy.make(Client, atelier=self.atelier)

    def test_first_name_label(self):
        field_label = self.client._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first Name')

    def test_last_name_label(self):
        field_label = self.client._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'second Name')

    def test_place_label(self):
        field_label = self.client._meta.get_field('place').verbose_name
        self.assertEquals(field_label, 'place')

    def test_atelier_label(self):
        field_label = self.client._meta.get_field('atelier').verbose_name
        self.assertEquals(field_label, 'atelier')

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
        self.assertEquals(self.client.get_absolute_url(), '/en/atelier/client/{}/'.format(id))


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
                          '/en/atelier/allowance_discount/{}/'.format(id))


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
        self.assertEquals(self.fabric_one.get_absolute_url(), '/en/atelier/fabric/{}/'.format(id))


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
                          '/en/atelier/complication_element/{}/'.format(id))


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
        self.assertEquals(self.minimal_style.get_absolute_url(), '/en/atelier/minimal_style/{}/'.format(id))


class ProductTestModel(TestCase):
    """
    Class to test the model
    Product
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.minimal_style = mommy.make('atelier.MinimalStyle')
        self.atelier = mommy.make(('atelier.Atelier'))
        self.product = mommy.make(Product, minimal_style=self.minimal_style, atelier=self.atelier)

    def test_instance(self):
        self.assertTrue(isinstance(self.product, Product))

    def test_relative_foreign_key(self):
        """
        if Product model foreign key related with MinimalStyle model   :return:true
        """
        self.assertEquals(self.product.minimal_style, self.minimal_style)
        self.assertEquals(self.product.atelier, self.atelier)

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.product.__str__(), self.product.name)

    def test_fields_verbose_name(self):
        field_name = self.product._meta.get_field('name').verbose_name
        field_minimal_style = self.product._meta.get_field('minimal_style').verbose_name
        field_base_price = self.product._meta.get_field('base_price').verbose_name
        field_atelier = self.product._meta.get_field('atelier').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_minimal_style, 'minimal style')
        self.assertEquals(field_base_price, 'base price')
        self.assertEquals(field_atelier, 'Atelier')

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
        self.assertEquals(self.product.get_absolute_url(), '/en/atelier/product/{}/'.format(id))


class OrderTestModel(TestCase):
    """
        Class to test the model
        Order
    """

    def setUp(self):
        """
        Set up all the tests
        """
        complication_element1 = mommy.make('atelier.ComplicationElement', base_price=10, complexity=2, name='Element1')
        complication_element2 = mommy.make('atelier.ComplicationElement', base_price=5, complexity=1, name='Element2')
        client = mommy.make('atelier.Client')
        product = mommy.make('atelier.Product', base_price=100)
        fabric = mommy.make('atelier.Fabric', complexity_factor=2)
        allowance_discount_1 = mommy.make('atelier.AllowanceDiscount', coefficient=1)
        allowance_discount_2 = mommy.make('atelier.AllowanceDiscount', coefficient=2)
        atelier = mommy.make('atelier.Atelier')
        user = mommy.make('User')
        self.order = mommy.make('atelier.Order', complication_elements=[complication_element1, complication_element2],
                                atelier=atelier, client=client, product=product, fabric=fabric,
                                allowance_discount=[allowance_discount_1, allowance_discount_2], performer=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.order, Order))

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.order.__str__(), ('{} {}'.format(self.order.client, self.order.order_date)))

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        id = self.order.id
        self.assertEquals(self.order.get_absolute_url(), '/en/atelier/order/{}/'.format(id))

    def test_fields_verbose_name(self):
        field_processing_category = self.order._meta.get_field('processing_category').verbose_name
        field_order_date = self.order._meta.get_field('order_date').verbose_name
        field_deadline = self.order._meta.get_field('deadline').verbose_name
        field_is_closed = self.order._meta.get_field('is_closed').verbose_name
        field_client = self.order._meta.get_field('client').verbose_name
        field_product = self.order._meta.get_field('product').verbose_name
        field_fabric = self.order._meta.get_field('fabric').verbose_name
        field_allowance_discount = self.order._meta.get_field('allowance_discount').verbose_name
        field_performer = self.order._meta.get_field('performer').verbose_name
        field_atelier = self.order._meta.get_field('atelier').verbose_name
        field_complication_elements = self.order._meta.get_field('complication_elements').verbose_name
        self.assertEquals(field_processing_category, 'processing category')
        self.assertEquals(field_order_date, 'order date')
        self.assertEquals(field_deadline, 'deadline')
        self.assertEquals(field_is_closed, 'closed')
        self.assertEquals(field_client, 'client')
        self.assertEquals(field_product, 'product')
        self.assertEquals(field_complication_elements, 'complication elements')
        self.assertEquals(field_fabric, 'fabric')
        self.assertEquals(field_allowance_discount, 'allowance/discount')
        self.assertEquals(field_performer, 'performer')
        self.assertEquals(field_atelier, 'atelier')

    def test_order_price(self):
        self.order.processing_category = 3
        self.assertEqual(self.order.order_price, '1000.00')


class AtelierTestModel(TestCase):
    """
        Class to test the model
        Atelier
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.atelier = mommy.make('atelier.Atelier')

    def test_instance(self):
        self.assertTrue(isinstance(self.atelier, Atelier))

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.atelier.__str__(), self.atelier.name)

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        id = self.atelier.id
        self.assertEquals(self.atelier.get_absolute_url(), '/en/atelier/atelier/{}/'.format(id))

    def test_fields_verbose_name(self):
        field_name = self.atelier._meta.get_field('name').verbose_name
        self.assertEquals(field_name, 'name')

    def test_field_arguments(self):
        max_length_name = self.atelier._meta.get_field('name').max_length
        self.assertEquals(max_length_name, 150)

class ProfileTestModel(TestCase):
    """
        Class to test the model
        Profile
    """

    def setUp(self):
        """
        Set up all the tests
        """
        user = mommy.make('User')
        self.profile = mommy.make('atelier.Profile', user=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_str_(self):
        """models _str_ checking"""
        self.assertEqual(self.profile.__str__(), self.profile.user.username)

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        id = self.profile.id
        self.assertEquals(self.profile.get_absolute_url(), '/en/atelier/profile/{}/'.format(id))

    def test_fields_verbose_name(self):
        field_user = self.profile._meta.get_field('user').verbose_name
        field_atelier = self.profile._meta.get_field('atelier').verbose_name
        field_is_tailor = self.profile._meta.get_field('is_tailor').verbose_name
        self.assertEquals(field_user, 'user')
        self.assertEquals(field_atelier, 'atelier')
        self.assertEquals(field_is_tailor, 'tailor')

    def test_field_arguments(self):
        help_text_is_tailor = self.profile._meta.get_field('is_tailor').help_text
        self.assertEquals(help_text_is_tailor, 'User can be a tailor to have administrator access within his atelier')

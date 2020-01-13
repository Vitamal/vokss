import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from atelier.forms import ProfileRegisterForm, ClientForm, ProfileChangeForm, AllowanceDiscountForm, AtelierForm, \
    ComplicationElementForm, FabricForm, MinimalStyleForm, OrderForm, ProductForm
from atelier.models import Profile, Client


class TestProfileRegisterForm(TestCase):

    def test_valid_form(self):
        data = {'username': 'user',
                'is_tailor': True,
                'email': 'email@ukr.net',
                'password1': 'UhdjY45tshj12',
                'password2': 'UhdjY45tshj12', }

        form = ProfileRegisterForm(data=data)
        print(form.error_messages)
        self.assertTrue(form.is_valid())

    def test_invalid_form_user_field(self):
        user = mommy.make(User, username='user', email='email@ukr.net', password='UhdjY45tshj12')
        data = {'username': 'user',  # A user with that username already exists.
                'is_tailor': True,
                'email': 'test@ukr.net',
                'password1': 'UhdjY45tshj12',
                'password2': 'UhdjY45tshj12', }

        form = ProfileRegisterForm(data=data)
        print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'username': ['A user with that username already exists.']})

    def test_invalid_form_email_field(self):
        user = mommy.make(User, username='user', email='email@ukr.net', password='UhdjY45tshj12')
        data = {'username': 'newuser',  # A user with that username already exists.
                'is_tailor': True,
                'email': 'email@ukr.net',
                'password1': 'UhdjY45tshj12',
                'password2': 'UhdjY45tshj12', }

        form = ProfileRegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Email Already Exists'])


class TestProfileChangeForm(TestCase):

    def test_valid_form(self):
        user = mommy.make(User, username='user', email='email@ukr.net', password='UhdjY45tshj12')
        profile = mommy.make(Profile, user=user, is_tailor=False)
        form = ProfileChangeForm({
            'is_tailor': True,
            'email': 'email@ukr.net',
        }, instance=profile)
        self.assertTrue(form.is_valid())


class TestClientForm(TestCase):

    def test_valid_client_form(self):
        data = {'first_name': 'John',
                'last_name': 'name',
                'tel_number': '123456',
                'place': 'place', }
        form = ClientForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_client_form(self):
        client = mommy.make('atelier.Client', first_name='name', last_name='last', tel_number=123456)
        data = {'first_name': client.first_name,
                'last_name': client.last_name,
                'tel_number': client.tel_number,
                'place': '', }
        form = ClientForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['place'], ['This field is required.'])


class TestAllowanceDiscountForm(TestCase):

    def test_valid_form(self):
        data = {'name': 'John',
                'coefficient': 1,
                'label': '123456'}
        form = AllowanceDiscountForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': 'John',
                'coefficient': 'coefficient',
                'label': '123456'}
        form = AllowanceDiscountForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['coefficient'], ['Enter a number.'])


class TestAtelierForm(TestCase):

    def test_valid_form(self):
        data = {'name': 'MyAtelier', }
        form = AtelierForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', }
        form = AtelierForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])


class TestComplicationElementForm(TestCase):

    def test_valid_form(self):
        data = {
            'name': 'John',
            'base_price': 1,
            'complexity': 2,
            'group': '2'
        }
        form = ComplicationElementForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': 'John',
            'base_price': 'A',
            'complexity': 2,
            'group': '2'
        }
        form = ComplicationElementForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['base_price'], ['Enter a number.'])

class TestFabricForm(TestCase):

    def test_valid_form(self):
        data = {
            'name': 'John',
            'complexity_factor': 1,
            'group': 'GR2'
        }
        form = FabricForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': 'John',
            'complexity_factor': 1,
            'group': '2'
        }
        form = FabricForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['group'], ['Select a valid choice. 2 is not one of the available choices.'])

class TestMinimalStyleForm(TestCase):

    def test_valid_form(self):
        data = {
            'name': 'John',
            'group': 'GR2'
        }
        form = MinimalStyleForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': 'John',
            'group': ''
        }
        form = MinimalStyleForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['group'], ['This field is required.'])

class TestOrderForm(TestCase):

    def test_valid_form(self):
        client = mommy.make('atelier.Client')
        product = mommy.make('atelier.Product')
        fabric = mommy.make('atelier.Fabric')
        complication_elements = mommy.make('atelier.ComplicationElement')
        allowance_discount = mommy.make('atelier.AllowanceDiscount')
        performer = mommy.make('User')
        now = datetime.datetime.now().date()

        data = {
            'client': client.pk,
            'product': product.pk,
            'fabric': fabric.pk,
            'processing_category': '1',
            'complication_elements': [complication_elements.pk],
            'allowance_discount': [allowance_discount.pk],
            'performer': performer.pk,
            'order_date': now,
            'deadline': now + datetime.timedelta(weeks=2),
            'is_closed': 'False',
        }
        form = OrderForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        client = mommy.make('atelier.Client')
        product = mommy.make('atelier.Product')
        fabric = mommy.make('atelier.Fabric')
        complication_elements = mommy.make('atelier.ComplicationElement')
        allowance_discount = mommy.make('atelier.AllowanceDiscount')
        performer = mommy.make('User')
        now = datetime.datetime.now().date()
        data = {
            'client': '',
            'product': product.pk,
            'fabric': fabric.pk,
            'processing_category': '1',
            'complication_elements': [complication_elements.pk],
            'allowance_discount': [allowance_discount.pk],
            'performer': performer.pk,
            'order_date': now,
            'deadline': now + datetime.timedelta(weeks=2),
            'is_closed': 'False',
        }
        form = OrderForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['client'], ['This field is required.'])

class TestProductForm(TestCase):

    def test_valid_form(self):
        m_s = mommy.make('atelier.MinimalStyle')
        data = {
            'name': 'John',
            'minimal_style': m_s.pk,
            'base_price': 100,
        }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        m_s = mommy.make('atelier.MinimalStyle')
        data = {
            'name': 'John',
            'minimal_style': m_s.pk,
            'base_price': '',
        }
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['base_price'], ['This field is required.'])

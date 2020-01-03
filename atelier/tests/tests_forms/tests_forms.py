from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy

from atelier.forms import ProfileRegisterForm, ClientForm
from atelier.models import Profile, Client


class TestProfileForm(TestCase):

    def test_valid_form(self):
        user = mommy.make(User, username='user', email='email@ukr.net', password='UhdjY45tshj12')
        profile = mommy.make(Profile, user=user, is_tailor=True)
        data = {'username': profile.user, 'is_tailor': profile.is_tailor, 'email': user.email,
                'password1': user.password, 'password2': user.password}
        form = ProfileRegisterForm(data=data)
        self.assertTrue(form.is_valid())


class TestClientForm(TestCase):

    def test_valid_client_form(self):
        client = mommy.make(Client, first_name='name', last_name='last', tel_number=123456, place='place')
        data = {'first_name': 'John', 'last_name': client.last_name, 'tel_number': client.tel_number,
                'place': client.place, }
        form = ClientForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_client_form(self):
        client = mommy.make(Client, first_name='name', last_name='last', tel_number=123456, place='')
        data = {'first_name': client.first_name, 'last_name': client.last_name, 'tel_number': client.tel_number,
                'place': client.place, }
        form = ClientForm(data=data)
        self.assertFalse(form.is_valid())

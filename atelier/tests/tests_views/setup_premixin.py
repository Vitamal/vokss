from django.test import TestCase

from django.contrib.auth.models import User
from model_mommy import mommy
from atelier.models import AllowanceDiscount, Profile


class SetUpPreMixin(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
            Create an instances for tests.
            The setUpTestData() allows the creation of initial data at the class level,
            once for the whole TestCase. This technique allows for faster tests as compared to using setUp()
        """
        cls.atelier = mommy.make('Atelier')
        cls.user = User.objects.create_user('user', 'lennon@thebeatles.com', 'userpassword')
        cls.tailor = User.objects.create_user('tailor', 'tailor@thebeatles.com', 'tailorpassword')
        cls.superuser = User.objects.create_user('superuser', 'jeck@thebeatles.com', 'supassword', is_superuser=True)
        cls.superuser_profile = mommy.make(Profile, user=cls.superuser, atelier=cls.atelier)
        cls.user_profile = mommy.make('Profile', user=cls.user, atelier=cls.atelier)
        cls.tailor_profile = mommy.make(Profile, user=cls.tailor, atelier=cls.atelier, is_tailor=True)

from django import test
from django.test import Client
from atelier.models import AllowanceDiscount


class SimpleTest(test.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase. Create one allowance_discount instance
        cls.allowance_discount = AllowanceDiscount.objects.create(name="Test", coefficient='1')

    def test_allowance_discount(self):

        # Issue a GET request.
        response = self.client.get('/uk/atelier/allowance_discount/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 allowance_discount.
        self.assertEqual(len(response.context['allowance_discount_list']), 1)


    # def test_language_using_cookie(self):
    #     self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'uk'})
    #     response = self.client.get('/atelier/allowance_discount/')
    #     self.assertEqual(response.content, b"allowance_discount")
    #
    # def test_language_using_header(self):
    #     response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='fr')
    #     self.assertEqual(response.content, b"Bienvenue sur mon site.")
    #
    # def test_language_using_override(self):
    #     with translation.override('fr'):
    #         response = self.client.get('/')
    #     self.assertEqual(response.content, b"Bienvenue sur mon site.")

class URLTests(test.TestCase):
    def test_homepage(self):
        response = self.client.get('/uk/atelier/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

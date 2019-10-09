from django.test import RequestFactory, TestCase
from model_mommy import mommy
from atelier.models import  AllowanceDiscount
from atelier.views import AllowanceDiscountDetailView

class PagesTest(TestCase):

    def test_index_page(self):
        response = self.client.get('/uk/atelier/')
        self.assertEqual(response.status_code, 200)

    def test_client_page(self):
        response = self.client.get('/en/atelier/client/')
        self.assertEqual(response.status_code, 200)

    def test_product_page(self):
        response = self.client.get('/en/atelier/product/')
        self.assertEqual(response.status_code, 200)

    def test_order_page(self):
        response = self.client.get('/en/atelier/order/')
        self.assertEqual(response.status_code, 200)

    def test_allowance_discount_page(self):
        response = self.client.get('/en/atelier/allowance_discount/')
        self.assertEqual(response.status_code, 200)

    def test_complication_element_page(self):
        response = self.client.get('/en/atelier/complication_element/')
        self.assertEqual(response.status_code, 200)

    def test_fabric_page(self):
        response = self.client.get('/en/atelier/fabric/')
        self.assertEqual(response.status_code, 200)

    def test_minimal_style_page(self):
        response = self.client.get('/en/atelier/minimal_style/')
        self.assertEqual(response.status_code, 200)

class GoodTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.allowance_discount = mommy.make(AllowanceDiscount)
    def test_allowance_discount_detail_view(self):
        # Create an instance of a GET request.
        pk = self.allowance_discount.pk
        request = self.factory.get('/en/atelier/allowance_discount/{}'.format(pk))
        # Test AllowanceDiscountDetailView() as if it were deployed at /en/atelier/allowance_discount/
        response = AllowanceDiscountDetailView.as_view()(request)
        self.assertEqual(response.status_code, 200)


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


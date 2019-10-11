from django.test import TestCase
from model_mommy import mommy
from atelier.models import AllowanceDiscount
from django.urls import reverse_lazy


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


class AllowanceDiscountViewTests(TestCase):
    def setUp(self):
        """Create an instances more than 10 for pagination tests"""
        self.allowance_discount = mommy.make(AllowanceDiscount, _quantity=13)

    def test_allowance_discount_detail_view(self):
        instance_id = self.allowance_discount[0].id
        response = self.client.get('/en/atelier/allowance_discount/{}/'.format(instance_id))  # get response in way one
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/allowance_discount_detail.html')

    def test_allowance_discount_view_form(self):
        response = self.client.get(reverse_lazy('atelier:allowance_discount_form'))  # get response in way two
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')

    def test_allowance_discount_edit_view(self):
        instance_id = self.allowance_discount[0].id
        response = self.client.get('/en/atelier/allowance_discount/{}/edit/'.format(instance_id))
        self.assertEqual(response.status_code, 200)

    def test_allowance_discount_delete_view(self):
        instance_id = self.allowance_discount[0].id
        response = self.client.get('/en/atelier/allowance_discount/{}/delete/'.format(instance_id))
        self.assertEqual(response.status_code, 200)

    def test_allowance_discount_list_view(self):
        response = self.client.get('/en/atelier/allowance_discount/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/allowance_discount_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse_lazy('atelier:allowance_discount_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['object_list']) == 10)



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

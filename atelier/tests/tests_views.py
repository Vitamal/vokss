import htmls
from django.test import TestCase
from model_mommy import mommy
from atelier.models import AllowanceDiscount
from django.urls import reverse_lazy


def _indent_string(string):
    try:
        return '\n'.join(['   {}'.format(line) for line in string.split('\n')])
    except:
        return string


class PagesTest(TestCase):

    def prettyformat_response_content(self, response):
        warnings = []
        output = None
        if hasattr(response, 'render'):
            try:
                response.render()
            except Exception as e:
                warnings.append('[cradmin TestCaseMixin warning] response.render() failed with: {}'.format(e))
            else:
                try:
                    output = '[cradmin TestCaseMixin info]: Prettyformatted response.content:\n{}'.format(
                        _indent_string(htmls.S(response.content).prettify())
                    )
                except:
                    pass
        if output is None:
            try:
                content = response.content.decode('utf-8')
            except UnicodeError:
                content = response.content
            if content:
                output = '[cradmin TestCaseMixin info]: response.content:\n{}'.format(
                    _indent_string(content))
            else:
                output = '[cradmin TestCaseMixin info]: response.content is empty.'
        return output, warnings

    def test_index_page_1(self):
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

    def test_index_page_2(self):
        """
            tests with using htmls module
        """
        response = self.client.get('/en/atelier/')
        selector = htmls.S(response.content)
        selector.list('h2')[0].prettyprint()     # print <h2>...</h2> first tag in terminal
        self.assertEqual(selector.one('h2').text_normalized, 'Welcome to Atelier!')

    def test_index_page_3(self):
        response = self.client.get('/en/atelier/')
        selector = htmls.S(response.content)
        self.assertEqual(len(selector.list('li')), 15)

    def test_index_page_4(self):
        response = self.client.get('/en/atelier/')
        selector = htmls.S(response.content)
        self.assertEqual(selector.one('title').alltext_normalized, "Atelier")


class AllowanceDiscountViewTests(TestCase):
    def setUp(self):
        """
            Create an instances more than 10 for pagination tests (13 instances)
        """
        self.allowance_discount = mommy.make(AllowanceDiscount, _quantity=13)

    def test_allowance_discount_detail_view(self):
        """
            In this test we get response in way one
        """
        instance_id = self.allowance_discount[0].id
        response = self.client.get('/en/atelier/allowance_discount/{}/'.format(instance_id))  # get response in way one
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/allowance_discount_detail.html')

    def test_allowance_discount_view_form(self):
        """
                In this test we get response in second way
        """
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

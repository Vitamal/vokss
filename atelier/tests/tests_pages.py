import htmls
from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from atelier.models import Profile
from django.urls import reverse

from atelier.tests.tests_views.setup_premixin import SetUpPreMixin


# def _indent_string(string):
#     try:
#         return '\n'.join(['   {}'.format(line) for line in string.split('\n')])
#     except:
#         return string


class LoginTestCase(SetUpPreMixin):

    def testLogin(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


class PagesTest(SetUpPreMixin):

    # def prettyformat_response_content(self, response):
    #     warnings = []
    #     output = None
    #     if hasattr(response, 'render'):
    #         try:
    #             response.render()
    #         except Exception as e:
    #             warnings.append('[cradmin TestCaseMixin warning] response.render() failed with: {}'.format(e))
    #         else:
    #             try:
    #                 output = '[cradmin TestCaseMixin info]: Prettyformatted response.content:\n{}'.format(
    #                     _indent_string(htmls.S(response.content).prettify())
    #                 )
    #             except:
    #                 pass
    #     if output is None:
    #         try:
    #             content = response.content.decode('utf-8')
    #         except UnicodeError:
    #             content = response.content
    #         if content:
    #             output = '[cradmin TestCaseMixin info]: response.content:\n{}'.format(
    #                 _indent_string(content))
    #         else:
    #             output = '[cradmin TestCaseMixin info]: response.content is empty.'
    #     return output, warnings

    def test_index_page_not_logged_in(self):
        response = self.client.get('/en/atelier/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_index_page_logged_in(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/')
        self.assertEqual(response.status_code, 200)

    def test_client_page_not_logged_in(self):
        response = self.client.get('/en/atelier/client/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_client_page_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/client/')
        self.assertEqual(response.status_code, 200)

    def test_product_page_not_logged_in(self):
        response = self.client.get('/en/atelier/product/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_product_page_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/product/')
        self.assertEqual(response.status_code, 200)

    def test_order_page_not_logged_in(self):
        response = self.client.get('/en/atelier/order/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_order_page(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/order/')
        self.assertEqual(response.status_code, 200)

    def test_allowance_discount_page_not_logged_in(self):
        response = self.client.get('/en/atelier/allowance_discount/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_allowance_discount_page(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/allowance_discount/')
        self.assertEqual(response.status_code, 200)

    def test_complication_element_page_not_logged_in(self):
        response = self.client.get('/en/atelier/complication_element/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_complication_element_page(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/complication_element/')
        self.assertEqual(response.status_code, 200)

    def test_fabric_page_not_logged_in(self):
        response = self.client.get('/en/atelier/fabric/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_fabric_page(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/fabric/')
        self.assertEqual(response.status_code, 200)

    def test_minimal_style_page_not_logged_in(self):
        response = self.client.get('/en/atelier/minimal_style/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_minimal_style_page(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/minimal_style/')
        self.assertEqual(response.status_code, 200)

    def test_profile_page_not_logged_in(self):
        response = self.client.get('/en/atelier/profile/')
        self.assertEqual(response.status_code, 404)

    def test_profile_page_not_tailor(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/profile/')
        self.assertEqual(response.status_code, 404)

    def test_profile_page_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.get('/en/atelier/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_page_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.get('/en/atelier/profile/')
        self.assertEqual(response.status_code, 200)

    def test_atelier_page_not_logged_in(self):
        response = self.client.get('/en/atelier/atelier/')
        self.assertEqual(response.status_code, 404)

    def test_atelier_page_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/atelier/')
        self.assertEqual(response.status_code, 404)

    def test_atelier_page_not_superuser(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.get('/en/atelier/atelier/')
        self.assertEqual(response.status_code, 404)

    def test_atelier_page_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.get('/en/atelier/atelier/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_2(self):
        """
            tests with using htmls module (see the docs here: https://github.com/espenak/htmls)
        """
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/')
        selector = htmls.S(response.content)
        selector.list('h2')[0].prettyprint()  # print <h2>...</h2> first tag in terminal
        self.assertEqual(selector.one('h2').text_normalized, 'Welcome to Atelier application!')

    def test_index_page_3(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/')
        selector = htmls.S(response.content)
        el = selector.one('.fa-home')
        print(el.alltext_normalized)
        self.assertEqual(len(selector.list('li')), 21)  # there is simple test for practice to use htmls

    def test_index_page_4(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/')
        selector = htmls.S(response.content)
        self.assertEqual(selector.one('title').alltext_normalized, "Atelier")

import htmls
from model_mommy import mommy
from atelier.models import Product, MinimalStyle
from django.urls import reverse_lazy
from atelier.tests.tests_views.setup_premixin import SetUpPreMixin


class ProductDetailViewTests(SetUpPreMixin):

    def test_client_detail_view_not_logged_in(self):
        item = mommy.make('atelier.Product')
        response = self.client.get(reverse_lazy('atelier:product_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_product_detail_view_user_not_in_atelier(self):
        self.client.login(username='user', password='userpassword')
        item = mommy.make('atelier.Product')
        response = self.client.get(reverse_lazy('atelier:product_detail', kwargs={'pk': item.pk, }))
        self.assertEqual(response.status_code, 404)

    def test_product_detail_view_tailor_not_in_atelier(self):
        self.client.login(username='tailor', password='tailorpassword')
        item = mommy.make('atelier.Product')
        response = self.client.get(reverse_lazy('atelier:product_detail', kwargs={'pk': item.pk, }))
        self.assertEqual(response.status_code, 404)

    def test_product_detail_view_user(self):
        '''
        test by the help of htmls module. (see https://github.com/espenak/htmls/)
        '''
        minimal_style = mommy.make(MinimalStyle)
        self.client.login(username='user', password='userpassword')
        kwargs = {
            'id': 1,
            'name': 'Product',
            'minimal_style': minimal_style,
            'base_price': 100,
            'atelier': self.user_profile.atelier,
        }
        instance = mommy.make('atelier.Product', **kwargs)
        response = self.client.get('/en/atelier/product/{}/'.format(instance.id))
        self.assertEqual(response.status_code, 200)
        selector = htmls.S(response.content)
        name = selector.one('.name').alltext_normalized
        minimal = selector.one('.minimal_style').alltext_normalized
        base_price = selector.one('.base_price').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(name, 'Product')
        self.assertEqual(minimal, minimal_style.group)
        self.assertEqual(base_price, '100.00 ₴')
        self.assertTemplateUsed(response, 'atelier/product_detail.html')


class ProductCreateViewTests(SetUpPreMixin):

    def test_product_create_view_not_logged_in(self):
        response = self.client.post(reverse_lazy('atelier:product_form'))
        self.assertEqual(response.status_code, 404)

    def test_product_create_view_not_tailor(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.post(reverse_lazy('atelier:product_form'))
        self.assertEqual(response.status_code, 404)

    def test_product_create_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:product_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')

    def test_product_create_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.post(reverse_lazy('atelier:product_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')


class ProductEditViewTests(SetUpPreMixin):

    def test_product_edit_view_not_logged_in(self):
        instance = mommy.make('atelier.Product')
        response = self.client.post(reverse_lazy('atelier:product_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_product_edit_view_not_tailor(self):
        self.client.login(username='user', password='supassword')
        instance = mommy.make('atelier.Product', atelier=self.user.profile.atelier)
        response = self.client.post(reverse_lazy('atelier:product_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_product_edit_view_tailor_not_in_atelier(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Product')
        response = self.client.post(reverse_lazy('atelier:product_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_product_edit_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        minimal_style = mommy.make(MinimalStyle)
        instance = mommy.make('atelier.Product', atelier=self.tailor.profile.atelier)
        response = self.client.post(
            reverse_lazy('atelier:product_update_form', kwargs={'pk': instance.id}),
            data={
                'name': 'Product',
                'minimal_style': minimal_style.id,
                'base_price': 100,
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/product/{}/'.format(instance.id))
        instance.refresh_from_db()
        self.assertEqual(instance.name, 'Product')
        self.assertEqual(instance.minimal_style, minimal_style)
        self.assertEqual(instance.base_price, 100)
        self.assertEqual(Product.objects.get(id=instance.id).last_updated_by, self.tailor)

    def test_product_edit_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        minimal_style = mommy.make(MinimalStyle)
        instance = mommy.make('atelier.Product', atelier=self.tailor.profile.atelier)
        response = self.client.post(
            reverse_lazy('atelier:product_update_form', kwargs={'pk': instance.id}),
            data={
                'name': 'Product',
                'minimal_style': minimal_style.id,
                'base_price': 100,
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/product/{}/'.format(instance.id))
        instance.refresh_from_db()
        self.assertEqual(instance.name, 'Product')
        self.assertEqual(instance.minimal_style, minimal_style)
        self.assertEqual(instance.base_price, 100)
        self.assertEqual(Product.objects.get(id=instance.id).last_updated_by, self.superuser)


class ProductDeleteViewTests(SetUpPreMixin):

    def test_product_delete_view_no_logged_in(self):
        instance = mommy.make('atelier.Product')
        response = self.client.get('/en/atelier/product/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_product_delete_view_not_tailor(self):
        self.client.login(username='user', password='userpassword')
        instance = mommy.make('atelier.Product', atelier=self.user.profile.atelier)
        response = self.client.get('/en/atelier/product/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_product_delete_view_tailor_not_in_atelier(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Product')
        response = self.client.get('/en/atelier/product/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_product_delete_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Product', atelier=self.tailor.profile.atelier)
        self.assertEqual(Product.objects.count(), 1)
        response = self.client.post('/en/atelier/product/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/product/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/product/')
        self.assertEqual(Product.objects.count(), 0)

    def test_product_delete_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        print(self.superuser.is_staff, self.superuser.is_superuser)
        instance = mommy.make('atelier.Product')
        self.assertEqual(Product.objects.count(), 1)
        response = self.client.post('/en/atelier/product/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/product/')
        self.assertRedirects(response, '/en/atelier/product/')
        self.assertEqual(Product.objects.count(), 0)


class ProductListViewTests(SetUpPreMixin):

    def test_product_list_view_no_logged_in(self):
        response = self.client.get('/en/atelier/product/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_product_list_view_user(self):
        '''
        test: user can see product list of his atelier only
        '''
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Product', atelier=self.user.profile.atelier, _quantity=3)
        mommy.make('atelier.Product', _quantity=7)
        response = self.client.get('/en/atelier/product/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/product_list.html')
        self.assertEqual(len(response.context['object_list']), 3)

    def test_product_list_view_superuser(self):
        '''
        test: superuser can see all products in all ateliers
        '''
        self.client.login(username='superuser', password='supassword')
        mommy.make('atelier.Product', _quantity=7)
        response = self.client.get('/en/atelier/product/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/product_list.html')
        self.assertEqual(len(response.context['object_list']), 7)

    def test_product_list_pagination_is_ten(self):
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Product', atelier=self.user.profile.atelier,
                   _quantity=13)  # Create an instances more than 10 for pagination tests (13 instances)
        resp = self.client.get(reverse_lazy('atelier:product_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 10)

    def test_product_list_all_elements(self):
        # get second page and confirm it has (exactly) remaining 3 items
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Product', atelier=self.user.profile.atelier,
                   _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:product_list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 3)

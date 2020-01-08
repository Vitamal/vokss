import htmls
from model_mommy import mommy
from atelier.models import ComplicationElement
from django.urls import reverse_lazy
from atelier.tests.tests_views.setup_premixin import SetUpPreMixin


class ComplicationElementDetailViewTests(SetUpPreMixin):

    def test_complication_element_detail_view_not_logged_in(self):
        item = mommy.make('atelier.ComplicationElement')
        response = self.client.get(reverse_lazy('atelier:complication_element_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_complication_element_detail_view_user(self):
        self.client.login(username='user', password='userpassword')
        kwargs = {
            'id': 1,
            'name': 'Name',
            'complexity': 2,
            'base_price': 100,
            'group': 'GR1',
        }
        instance = mommy.make('atelier.ComplicationElement', **kwargs)
        response = self.client.get(
            '/en/atelier/complication_element/{}/'.format(instance.id))  # get response in way one
        selector = htmls.S(response.content)
        name = selector.one('.name').alltext_normalized
        complexity = selector.one('.complexity').alltext_normalized
        group = selector.one('.group').alltext_normalized
        base_price = selector.one('.base_price').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(complexity, '2.00')
        self.assertEqual(group, 'GR1')
        self.assertEqual(base_price, '100.00')
        self.assertEqual(name, 'Name')
        self.assertTemplateUsed(response, 'atelier/complication_element_detail.html')


class ComplicationElementCreateViewTests(SetUpPreMixin):

    def test_complication_element_create_view_not_logged_in(self):
        response = self.client.post(reverse_lazy('atelier:complication_element_form'))
        self.assertEqual(response.status_code, 404)

    def test_complication_element_create_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:complication_element_form'))
        self.assertEqual(response.status_code, 404)

    def test_complication_element_create_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.post(reverse_lazy('atelier:complication_element_form'))  # get response in way two
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')


class ComplicationElementEditViewTests(SetUpPreMixin):

    def test_complication_element_edit_view_not_logged_in(self):
        instance = mommy.make('atelier.ComplicationElement')
        response = self.client.post(
            reverse_lazy('atelier:complication_element_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_complication_element_edit_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.ComplicationElement')
        response = self.client.post(
            reverse_lazy('atelier:complication_element_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_complication_element_edit_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.ComplicationElement', name='Name')
        response = self.client.post(
            reverse_lazy('atelier:complication_element_update_form', kwargs={'pk': instance.id}),
            data={
                'name': 'SomeName',
                'complexity': 2,
                'base_price': 100,
                'group': 'GR1',
                'last_updated_by': 'user',
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/complication_element/{}/'.format(instance.id))
        instance.refresh_from_db()
        self.assertEqual(ComplicationElement.objects.count(), 1)
        self.assertEqual(ComplicationElement.objects.get(id=instance.id), instance)
        self.assertEqual(ComplicationElement.objects.get(id=instance.id).name, 'SomeName')


class ComplicationElementDeleteViewTests(SetUpPreMixin):

    def test_complication_element_delete_view_no_logged_in(self):
        instance = mommy.make('atelier.ComplicationElement')
        response = self.client.get('/en/atelier/complication_element/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_complication_element_delete_view_user(self):
        self.client.login(username='user', password='userpassword')
        instance = mommy.make('atelier.ComplicationElement')
        response = self.client.get('/en/atelier/complication_element/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_complication_element_delete_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.ComplicationElement')
        response = self.client.get('/en/atelier/complication_element/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_complication_element_delete_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.ComplicationElement')
        self.assertEqual(ComplicationElement.objects.count(), 1)
        response = self.client.post('/en/atelier/complication_element/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/complication_element/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/complication_element/')
        self.assertEqual(ComplicationElement.objects.count(), 0)


class ComplicationElementListViewTests(SetUpPreMixin):

    def test_complication_element_list_view_no_logged_in(self):
        response = self.client.get('/en/atelier/complication_element/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_complication_element_list_view_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/complication_element/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/complication_element_list.html')

    def test_complication_element_list_pagination_is_ten(self):
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.ComplicationElement', _quantity=13)
        # Create an instances more than 10 for pagination tests (13 instances)
        resp = self.client.get(reverse_lazy('atelier:complication_element_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertTrue(len(resp.context['object_list']) == 10)

    def test_complication_element_list_all_elements(self):
        # get second page and confirm it has (exactly) remaining 3 items
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.ComplicationElement',
                   _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:complication_element_list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 3)

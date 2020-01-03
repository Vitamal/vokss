import htmls
from model_mommy import mommy
from atelier.models import Atelier
from django.urls import reverse_lazy

from atelier.tests.tests_views.setup_premixin import SetUpPreMixin


class AtelierViewTests(SetUpPreMixin):

    def test_atelier_detail_view_not_logged_in(self):
        item = mommy.make(Atelier)
        response = self.client.get(reverse_lazy('atelier:atelier_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 404)

    def test_atelier_detail_view_user(self):
        self.client.login(username='user', password='userpassword')
        item = mommy.make(Atelier)
        response = self.client.get(reverse_lazy('atelier:atelier_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 404)

    def test_atelier_detail_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        item = mommy.make(Atelier)
        response = self.client.get(reverse_lazy('atelier:atelier_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 404)

    def test_atelier_detail_view_superuser(self):
        '''
        test by the help of htmls module. (see https://github.com/espenak/htmls/)
        '''
        self.client.login(username='superuser', password='supassword')
        kwargs = {
            'id': 1,
            'name': 'super_atelier',
        }
        instance = mommy.make(Atelier, **kwargs)
        response = self.client.get('/en/atelier/atelier/{}/'.format(instance.id))
        selector = htmls.S(response.content)
        name = selector.one('.name').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(name, 'Ateliers: super_atelier')
        self.assertTemplateUsed(response, 'atelier/atelier_detail.html')

    def test_atelier_create_view_not_logged_in(self):
        response = self.client.post(reverse_lazy('atelier:atelier_form'))
        self.assertEqual(response.status_code, 404)

    def test_client_create_view_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.post(reverse_lazy('atelier:atelier_form'))
        self.assertEqual(response.status_code, 404)

    def test_atelier_create_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:atelier_form'))
        self.assertEqual(response.status_code, 404)

    def test_atelier_create_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.post(reverse_lazy('atelier:atelier_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')

    def test_atelier_edit_view_not_logged_in(self):
        instance = mommy.make(Atelier)
        response = self.client.post(reverse_lazy('atelier:atelier_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_atelier_edit_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make(Atelier)
        response = self.client.post(reverse_lazy('atelier:atelier_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_atelier_edit_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make(Atelier)
        response = self.client.post(
            reverse_lazy('atelier:atelier_update_form', kwargs={'pk': instance.id}),
            data={
                'name': 'Superatelier',
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/atelier/{}/'.format(instance.id))
        instance.refresh_from_db()
        self.assertEqual(instance.name, 'Superatelier')

    def test_atelier_delete_view_no_logged_in(self):
        instance = mommy.make(Atelier)
        response = self.client.get('/en/atelier/atelier/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_atelier_delete_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make(Atelier)
        response = self.client.get('/en/atelier/atelier/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_atelier_delete_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make(Atelier)
        self.assertEqual(Atelier.objects.count(), 2)  # + 1 instance from SetUpPreMixin
        response = self.client.post('/en/atelier/atelier/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/atelier/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/atelier/')
        self.assertEqual(Atelier.objects.count(), 1)

    def test_atelier_list_view_no_logged_in(self):
        response = self.client.get('/en/atelier/client/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_atelier_list_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.get('/en/atelier/atelier/')
        self.assertEqual(response.status_code, 404)

    def test_atelier_list_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        mommy.make(Atelier)
        response = self.client.get('/en/atelier/atelier/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/atelier_list.html')
        self.assertEqual(len(response.context['object_list']), 2)  # + 1 instance from SetUpPreMixin

    def test_atelier_pagination_is_ten(self):
        self.client.login(username='superuser', password='supassword')
        # Create an instances more than 10 for pagination tests (13 instances)
        self.allowance_discount = mommy.make(Atelier, _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:atelier_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 10)

    def test_atelier_list_all_elements(self):
        # get second page and confirm it has (exactly) remaining 3 items
        self.client.login(username='superuser', password='supassword')
        self.allowance_discount = mommy.make(Atelier, _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:atelier_list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 4)  # + 1 instance from SetUpPreMixin

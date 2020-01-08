import htmls
from model_mommy import mommy
from atelier.models import Client
from django.urls import reverse_lazy
from atelier.tests.tests_views.setup_premixin import SetUpPreMixin


class ClientDetailViewTests(SetUpPreMixin):

    def test_client_detail_view_not_logged_in(self):
        item = mommy.make('atelier.Client')
        response = self.client.get(reverse_lazy('atelier:client_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_client_detail_view_tailor_not_in_atelier(self):
        self.client.login(username='tailor', password='tailorpassword')
        item = mommy.make('atelier.Client')
        response = self.client.get(reverse_lazy('atelier:client_detail', kwargs={'pk': item.pk, }))
        self.assertEqual(response.status_code, 404)

    def test_client_detail_view_user(self):
        '''
        test by the help of htmls module. (see https://github.com/espenak/htmls/)
        '''
        self.client.login(username='user', password='userpassword')
        kwargs = {
            'id': 1,
            'first_name': 'Ivan',
            'last_name': 'Sakh',
            'tel_number': 123456,
            'place': 'Kyiv',
            'atelier': self.user_profile.atelier,
        }
        instance = mommy.make('atelier.Client', **kwargs)
        response = self.client.get('/en/atelier/client/{}/'.format(instance.id))
        selector = htmls.S(response.content)
        first = selector.one('.first').alltext_normalized
        last = selector.one('.last').alltext_normalized
        tel = selector.one('.tel').alltext_normalized
        pl = selector.one('.pl').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(first, 'Ivan')
        self.assertEqual(last, 'Sakh')
        self.assertEqual(tel, '123456')
        self.assertEqual(pl, 'Kyiv')
        self.assertTemplateUsed(response, 'atelier/client_detail.html')


class ClientCreateViewTests(SetUpPreMixin):

    def test_client_create_view_not_logged_in(self):
        response = self.client.post(reverse_lazy('atelier:client_form'))
        self.assertEqual(response.status_code, 404)

    def test_client_create_view_not_tailor(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.post(reverse_lazy('atelier:client_form'))
        self.assertEqual(response.status_code, 404)

    def test_client_create_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:client_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')

    def test_client_create_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.post(reverse_lazy('atelier:client_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')


class ClientEditViewTests(SetUpPreMixin):

    def test_client_edit_view_not_logged_in(self):
        instance = mommy.make('atelier.Client')
        response = self.client.post(reverse_lazy('atelier:client_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_client_edit_view_not_tailor(self):
        self.client.login(username='user', password='supassword')
        instance = mommy.make('atelier.Client', atelier=self.user.profile.atelier)
        response = self.client.post(reverse_lazy('atelier:client_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_client_edit_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Client', atelier=self.tailor.profile.atelier)
        response = self.client.post(
            reverse_lazy('atelier:client_update_form', kwargs={'pk': instance.id}),
            data={
                'first_name': 'Sashko',
                'last_name': 'Fritz',
                'tel_number': '123456',
                'place': 'Morshyn',
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/client/{}/'.format(instance.id))
        instance.refresh_from_db()
        self.assertEqual(instance.first_name, 'Sashko')
        self.assertEqual(instance.tel_number, '123456')
        self.assertEqual(instance.last_name, 'Fritz')
        self.assertEqual(instance.place, 'Morshyn')
        self.assertEqual(Client.objects.get(id=instance.id).last_updated_by, self.tailor)

    def test_client_edit_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.Client', atelier=self.atelier)
        response = self.client.post(
            reverse_lazy('atelier:client_update_form', kwargs={'pk': instance.id}),
            data={
                'first_name': 'Ivan',
                'last_name': 'Sakh',
                'tel_number': 123456,
                'place': 'Kyiv',
            })
        print(response['Location'])
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/client/{}/'.format(instance.id))
        instance.refresh_from_db()
        self.assertEqual(instance.first_name, 'Ivan')
        self.assertEqual(instance.last_name, 'Sakh')
        self.assertEqual(instance.tel_number, '123456')
        self.assertEqual(instance.place, 'Kyiv')
        self.assertEqual(instance.last_updated_by, self.superuser)


class ClientDeleteViewTests(SetUpPreMixin):

    def test_client_delete_view_no_logged_in(self):
        instance = mommy.make('atelier.Client')
        response = self.client.get('/en/atelier/client/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_client_delete_view_not_tailor(self):
        self.client.login(username='user', password='userpassword')
        instance = mommy.make('atelier.Client', atelier=self.user.profile.atelier)
        response = self.client.get('/en/atelier/client/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_client_delete_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Client', atelier=self.tailor.profile.atelier)
        self.assertEqual(Client.objects.count(), 1)
        response = self.client.post('/en/atelier/client/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/client/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/client/')
        self.assertEqual(Client.objects.count(), 0)

    def test_client_delete_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.Client', atelier=self.atelier)
        self.assertEqual(Client.objects.count(), 1)
        response = self.client.post('/en/atelier/client/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/client/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/client/')
        self.assertEqual(Client.objects.count(), 0)


class ClientListViewTests(SetUpPreMixin):

    def test_client_list_view_no_logged_in(self):
        response = self.client.get('/en/atelier/client/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_client_list_view_user(self):
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Client', atelier=self.user.profile.atelier, _quantity=4)
        mommy.make('atelier.Client', _quantity=6)
        response = self.client.get('/en/atelier/client/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/client_list.html')
        self.assertEqual(len(response.context['object_list']), 4)

    def test_client_list_pagination_is_ten(self):
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Client', atelier=self.user.profile.atelier,
                   _quantity=13)  # Create an instances more than 10 for pagination tests (13 instances)
        resp = self.client.get(reverse_lazy('atelier:client_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 10)

    def test_client_list_all_elements(self):
        # get second page and confirm it has (exactly) remaining 3 items
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Client', atelier=self.user.profile.atelier,
                   _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:client_list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 3)

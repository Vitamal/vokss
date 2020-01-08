import htmls
from model_mommy import mommy
from atelier.models import MinimalStyle
from django.urls import reverse_lazy
from atelier.tests.tests_views.setup_premixin import SetUpPreMixin


class MinimalStyleViewTests(SetUpPreMixin):

    def test_minimal_style_detail_view_not_logged_in(self):
        item = mommy.make('atelier.MinimalStyle')
        response = self.client.get(reverse_lazy('atelier:minimal_style_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_minimal_style_detail_view_user(self):
        self.client.login(username='user', password='userpassword')
        kwargs = {
            'id': 1,
            'name': 'MSName',
            'group': 'Group1',
        }
        instance = mommy.make('atelier.MinimalStyle', **kwargs)
        response = self.client.get('/en/atelier/minimal_style/{}/'.format(instance.id))  # get response in way one
        selector = htmls.S(response.content)
        name = selector.one('.name').alltext_normalized
        group = selector.one('.group').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(group, 'Group1')
        self.assertEqual(name, 'MSName')
        self.assertTemplateUsed(response, 'atelier/minimal_style_detail.html')


class MinimalStyleCreateViewTests(SetUpPreMixin):

    def test_minimal_style_create_view_not_logged_in(self):
        response = self.client.post(reverse_lazy('atelier:minimal_style_form'))
        self.assertEqual(response.status_code, 404)

    def test_minimal_style_create_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:minimal_style_form'))
        self.assertEqual(response.status_code, 404)

    def test_minimal_style_create_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.post(reverse_lazy('atelier:minimal_style_form'))  # get response in way two
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')


class MinimalStyleEditViewTests(SetUpPreMixin):

    def test_minimal_style_edit_view_not_logged_in(self):
        instance = mommy.make('atelier.MinimalStyle')
        response = self.client.post(reverse_lazy('atelier:minimal_style_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_minimal_style_edit_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.MinimalStyle')
        response = self.client.post(reverse_lazy('atelier:minimal_style_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_minimal_style_edit_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.MinimalStyle', name='Name', group='GR0')
        response = self.client.post(
            reverse_lazy('atelier:minimal_style_update_form', kwargs={'pk': instance.id}),
            data={
                'name': 'MSName',
                'group': 'Group1',
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/minimal_style/{}/'.format(instance.id))
        instance.refresh_from_db()
        self.assertEqual(MinimalStyle.objects.count(), 1)
        self.assertEqual(MinimalStyle.objects.get(id=instance.id), instance)
        self.assertEqual(MinimalStyle.objects.get(id=instance.id).name, 'MSName')
        self.assertEqual(MinimalStyle.objects.get(id=instance.id).group, 'Group1')
        self.assertEqual(MinimalStyle.objects.get(id=instance.id).last_updated_by, self.superuser)


class MinimalStyleDeleteViewTests(SetUpPreMixin):

    def test_minimal_style_delete_view_no_logged_in(self):
        instance = mommy.make('atelier.MinimalStyle')
        response = self.client.get('/en/atelier/minimal_style/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_minimal_style_delete_view_user(self):
        self.client.login(username='user', password='userpassword')
        instance = mommy.make('atelier.MinimalStyle')
        response = self.client.get('/en/atelier/minimal_style/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_minimal_style_delete_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.MinimalStyle')
        response = self.client.get('/en/atelier/minimal_style/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_minimal_style_delete_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.MinimalStyle')
        self.assertEqual(MinimalStyle.objects.count(), 1)
        response = self.client.post('/en/atelier/minimal_style/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/minimal_style/')
        self.assertEqual(MinimalStyle.objects.count(), 0)


class MinimalStyleListViewTests(SetUpPreMixin):

    def test_minimal_style_list_view_no_logged_in(self):
        response = self.client.get('/en/atelier/minimal_style/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_minimal_style_list_view_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/minimal_style/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/minimal_style_list.html')

    def test_minimal_style_list_pagination_is_ten(self):
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.MinimalStyle', _quantity=13)
        # Create an instances more than 10 for pagination tests (13 instances)
        resp = self.client.get(reverse_lazy('atelier:minimal_style_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertTrue(len(resp.context['object_list']) == 10)

    def test_minimal_style_list_all_elements(self):
        # get second page and confirm it has (exactly) remaining 3 items
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.MinimalStyle',
                   _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:minimal_style_list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 3)

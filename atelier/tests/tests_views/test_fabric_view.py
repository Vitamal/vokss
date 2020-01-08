import htmls
from model_mommy import mommy
from atelier.models import Fabric
from django.urls import reverse_lazy
from atelier.tests.tests_views.setup_premixin import SetUpPreMixin


class FabricDetailViewTests(SetUpPreMixin):

    def test_fabric_detail_view_not_logged_in(self):
        item = mommy.make('atelier.Fabric')
        response = self.client.get(reverse_lazy('atelier:fabric_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_fabric_detail_view_user(self):
        self.client.login(username='user', password='userpassword')
        kwargs = {
            'id': 1,
            'name': 'Name',
            'complexity_factor': 2,
            'group': 'GR1',  # choice field
        }
        instance = mommy.make('atelier.Fabric', **kwargs)
        response = self.client.get('/en/atelier/fabric/{}/'.format(instance.id))  # get response in way one
        selector = htmls.S(response.content)
        name = selector.one('.name').alltext_normalized
        factor = selector.one('.factor').alltext_normalized
        group = selector.one('.group').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(factor, '2.00')
        self.assertEqual(group, 'GR1')
        self.assertEqual(name, 'Name')
        self.assertTemplateUsed(response, 'atelier/fabric_detail.html')


class FabricCreateViewTests(SetUpPreMixin):

    def test_fabric_create_view_not_logged_in(self):
        response = self.client.post(reverse_lazy('atelier:fabric_form'))
        self.assertEqual(response.status_code, 404)

    def test_fabric_create_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:fabric_form'))
        self.assertEqual(response.status_code, 404)

    def test_fabric_create_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.post(reverse_lazy('atelier:fabric_form'))  # get response in way two
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')


class FabricEditViewTests(SetUpPreMixin):

    def test_fabric_edit_view_not_logged_in(self):
        instance = mommy.make('atelier.Fabric')
        response = self.client.post(reverse_lazy('atelier:fabric_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_fabric_edit_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Fabric')
        response = self.client.post(reverse_lazy('atelier:fabric_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_fabric_edit_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.Fabric', name='Name', complexity_factor=1, group='GR0')
        response = self.client.post(
            reverse_lazy('atelier:fabric_update_form', kwargs={'pk': instance.id}),
            data={
                'name': 'OtherName',
                'complexity_factor': 2,
                'group': 'GR1',  # choice field
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/fabric/{}/'.format(instance.id))
        instance.refresh_from_db()
        self.assertEqual(Fabric.objects.count(), 1)
        self.assertEqual(Fabric.objects.get(id=instance.id), instance)
        self.assertEqual(Fabric.objects.get(id=instance.id).name, 'OtherName')
        self.assertEqual(Fabric.objects.get(id=instance.id).complexity_factor, 2.00)
        self.assertEqual(Fabric.objects.get(id=instance.id).group, 'GR1')
        self.assertEqual(Fabric.objects.get(id=instance.id).last_updated_by, self.superuser)


class FabricDeleteViewTests(SetUpPreMixin):

    def test_fabric_delete_view_no_logged_in(self):
        instance = mommy.make('atelier.Fabric')
        response = self.client.get('/en/atelier/fabric/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_fabric_delete_view_user(self):
        self.client.login(username='user', password='userpassword')
        instance = mommy.make('atelier.Fabric')
        response = self.client.get('/en/atelier/fabric/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_fabric_delete_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Fabric')
        response = self.client.get('/en/atelier/fabric/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_fabric_delete_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.Fabric')
        self.assertEqual(Fabric.objects.count(), 1)
        response = self.client.post('/en/atelier/fabric/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/fabric/')
        self.assertEqual(Fabric.objects.count(), 0)


class FabricListViewTests(SetUpPreMixin):

    def test_fabric_list_view_no_logged_in(self):
        response = self.client.get('/en/atelier/fabric/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_fabric_list_view_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/fabric/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/fabric_list.html')

    def test_fabric_list_pagination_is_ten(self):
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Fabric', _quantity=13)
        # Create an instances more than 10 for pagination tests (13 instances)
        resp = self.client.get(reverse_lazy('atelier:fabric_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertTrue(len(resp.context['object_list']) == 10)

    def test_fabric_list_all_elements(self):
        # get second page and confirm it has (exactly) remaining 3 items
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Fabric',
                   _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:fabric_list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 3)

import htmls
from model_mommy import mommy
from atelier.models import AllowanceDiscount
from django.urls import reverse_lazy
from django.utils import timezone

from atelier.tests.tests_views.setup_premixin import SetUpPreMixin


class AllowanceDiscountViewTests(SetUpPreMixin):

    def test_allowance_discount_detail_view_not_logged_in(self):
        item = mommy.make(AllowanceDiscount)
        response = self.client.get(reverse_lazy('atelier:allowance_discount_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_allowance_discount_detail_view(self):
        self.client.login(username='user', password='userpassword')
        kwargs = {
            'id': 1,
            'name': 'Name',
            'coefficient': 1,
            'label': 'Label',
        }
        instance = mommy.make(AllowanceDiscount, **kwargs)
        response = self.client.get('/en/atelier/allowance_discount/{}/'.format(instance.id))  # get response in way one
        selector = htmls.S(response.content)
        type = selector.one('.type').alltext_normalized
        coefficient = selector.one('.coefficient').alltext_normalized
        name = selector.one('.name').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type, 'Label')
        self.assertEqual(coefficient, '1.00')
        self.assertEqual(name, 'Name')
        self.assertTemplateUsed(response, 'atelier/allowance_discount_detail.html')

    def test_allowance_discount_create_view_not_logged_in(self):
        response = self.client.post(reverse_lazy('atelier:allowance_discount_form'))
        self.assertEqual(response.status_code, 404)

    def test_allowance_discount_create_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:allowance_discount_form'))
        self.assertEqual(response.status_code, 404)

    def test_allowance_discount_create_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.post(reverse_lazy('atelier:allowance_discount_form'))  # get response in way two
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')

    def test_allowance_discount_edit_view_not_logged_in(self):
        instance = mommy.make(AllowanceDiscount)
        response = self.client.post(reverse_lazy('atelier:allowance_discount_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_allowance_discount_edit_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make(AllowanceDiscount)
        response = self.client.post(reverse_lazy('atelier:allowance_discount_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_allowance_discount_edit_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make(AllowanceDiscount, name='Name')
        response = self.client.post(
            reverse_lazy('atelier:allowance_discount_update_form', kwargs={'pk': instance.id}),
            data={
                'name': 'SomeName',
                'coefficient': 1.23,
                'label': 'SomeLabel',
                'last_updated_datetime': timezone.now(),
                'last_updated_by': 'user',
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/allowance_discount/{}/'.format(instance.id))
        instance.refresh_from_db()
        self.assertEqual(AllowanceDiscount.objects.count(), 1)
        self.assertEqual(AllowanceDiscount.objects.get(id=instance.id), instance)
        self.assertEqual(AllowanceDiscount.objects.get(id=instance.id).name, 'SomeName')

    def test_allowance_discount_delete_view_no_logged_in(self):
        instance = mommy.make(AllowanceDiscount)
        response = self.client.get('/en/atelier/allowance_discount/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_allowance_discount_delete_view_user(self):
        self.client.login(username='user', password='userpassword')
        instance = mommy.make(AllowanceDiscount)
        response = self.client.get('/en/atelier/allowance_discount/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_allowance_discount_delete_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make(AllowanceDiscount)
        response = self.client.get('/en/atelier/allowance_discount/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_allowance_discount_delete_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make(AllowanceDiscount)
        self.assertEqual(AllowanceDiscount.objects.count(), 1)
        response = self.client.post('/en/atelier/allowance_discount/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/allowance_discount/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/allowance_discount/')
        self.assertEqual(AllowanceDiscount.objects.count(), 0)

    def test_allowance_discount_list_view_no_logged_in(self):
        response = self.client.get('/en/atelier/allowance_discount/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_allowance_discount_list_view_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get('/en/atelier/allowance_discount/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/allowance_discount_list.html')

    def test_allowance_discount_list_pagination_is_ten(self):
        self.client.login(username='user', password='userpassword')
        self.allowance_discount = mommy.make(AllowanceDiscount, _quantity=13)
        # Create an instances more than 10 for pagination tests (13 instances)
        resp = self.client.get(reverse_lazy('atelier:allowance_discount_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertTrue(len(resp.context['object_list']) == 10)

    def test_allowance_discount_list_all_elements(self):
        # get second page and confirm it has (exactly) remaining 3 items
        self.client.login(username='user', password='userpassword')
        self.allowance_discount = mommy.make(AllowanceDiscount,
                                             _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:allowance_discount_list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 3)

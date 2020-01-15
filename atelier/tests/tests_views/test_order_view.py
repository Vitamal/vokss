import htmls
from model_mommy import mommy
from atelier.models import Order
from django.urls import reverse_lazy
from atelier.tests.tests_views.setup_premixin import SetUpPreMixin
import datetime


class OrderDetailViewTests(SetUpPreMixin):

    def test_client_detail_view_not_logged_in(self):
        item = mommy.make('atelier.Order')
        response = self.client.get(reverse_lazy('atelier:order_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_order_detail_view_tailor_not_in_atelier(self):
        self.client.login(username='tailor', password='tailorpassword')
        item = mommy.make('atelier.Order')
        response = self.client.get(reverse_lazy('atelier:order_detail', kwargs={'pk': item.pk, }))
        self.assertEqual(response.status_code, 404)

    def test_order_detail_view_user(self):
        '''
        test by the help of htmls module. (see https://github.com/espenak/htmls/)
        '''
        self.client.login(username='user', password='userpassword')
        client = mommy.make('atelier.Client')
        product = mommy.make('atelier.Product')
        fabric = mommy.make('atelier.Fabric')
        complication_elements = mommy.make('atelier.ComplicationElement', _quantity=2)
        allowance_discount = mommy.make('atelier.AllowanceDiscount', _quantity=3)
        kwargs = {
            'id': 1,
            'client': client,
            'product': product,
            'fabric': fabric,
            'processing_category': '1',
            'complication_elements': complication_elements,
            'allowance_discount': allowance_discount,
            'order_date': datetime.date.today,
            'performer': self.user,
            'deadline': datetime.datetime.now() + datetime.timedelta(weeks=2),
            'atelier': self.user_profile.atelier,
        }
        instance = mommy.make('atelier.Order', **kwargs)
        response = self.client.get('/en/atelier/order/{}/'.format(instance.id))
        self.assertEqual(response.status_code, 200)
        formated_deadline = (datetime.datetime.now() + datetime.timedelta(weeks=2)).strftime('%b. %d, %Y')
        formated_date = datetime.datetime.now().strftime('%A %d %B %Y')
        selector = htmls.S(response.content)
        s_client = selector.one('.client').alltext_normalized
        s_product = selector.one('.product').alltext_normalized
        s_fabric = selector.one('.fabric').alltext_normalized
        s_fabric_group = selector.one('.fabric_group').alltext_normalized
        s_complication_elements = selector.count('.elements')
        s_processing_category = selector.one('.category').alltext_normalized
        s_allowance_discount = selector.count('.discount')
        s_order_date = selector.one('.date').alltext_normalized
        s_performer = selector.one('.performer').alltext_normalized
        s_deadline = selector.one('.deadline').alltext_normalized
        s_closed = selector.one('.closed').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(s_client, client.first_name + ' ' + client.last_name)
        self.assertEqual(s_product, product.name)
        self.assertEqual(s_fabric, fabric.name)
        self.assertEqual(s_fabric_group, fabric.group)
        self.assertEqual(s_processing_category, '1')
        self.assertEqual(s_complication_elements, 2)
        self.assertEqual(s_allowance_discount, 3)
        self.assertEqual(s_order_date, formated_date)
        self.assertEqual(s_performer, self.user.username)
        self.assertEqual(s_closed, 'No')
        self.assertEqual(s_deadline, formated_deadline)
        self.assertTemplateUsed(response, 'atelier/order_detail.html')


class OrderCreateViewTests(SetUpPreMixin):

    def test_order_create_view_not_logged_in(self):
        response = self.client.post(reverse_lazy('atelier:order_form'))
        self.assertEqual(response.status_code, 404)

    def test_order_create_view_not_tailor(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.post(reverse_lazy('atelier:order_form'))
        self.assertEqual(response.status_code, 404)

    def test_order_create_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:order_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/order_form.html')

    def test_order_create_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.post(reverse_lazy('atelier:order_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/order_form.html')

    def test_order_create_view_fields_filtering(self):
        # the tailor can choose instanses of his own atelier only (for ForeignKey fields)
        mommy.make('atelier.Client', _quantity=3)
        mommy.make('atelier.Product', _quantity=3)
        mommy.make('atelier.Profile', _quantity=3)
        mommy.make('atelier.Client', atelier=self.atelier, _quantity=2)
        mommy.make('atelier.Product', atelier=self.atelier, _quantity=4)
        mommy.make('atelier.Profile', atelier=self.atelier, _quantity=6)
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:order_form'))
        self.assertEqual(response.context_data['form'].fields['client'].queryset.count(), 2)
        self.assertEqual(response.context_data['form'].fields['product'].queryset.count(), 4)
        self.assertEqual(response.context_data['form'].fields['performer'].queryset.count(), 6)


class OrderEditViewTests(SetUpPreMixin):

    def test_order_edit_view_not_logged_in(self):

        instance = mommy.make('atelier.Order')
        response = self.client.post(reverse_lazy('atelier:order_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_order_edit_view_not_tailor(self):
        self.client.login(username='user', password='supassword')
        instance = mommy.make('atelier.Order', atelier=self.user.profile.atelier)
        response = self.client.post(reverse_lazy('atelier:order_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_order_edit_view_tailor_not_in_atelier(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Order')
        response = self.client.post(reverse_lazy('atelier:order_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_order_edit_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        order = mommy.make('atelier.Order', atelier=self.tailor.profile.atelier)
        my_client = mommy.make('atelier.Client')
        product = mommy.make('atelier.Product')
        fabric = mommy.make('atelier.Fabric')
        complication_elements = mommy.make('atelier.ComplicationElement', _quantity=2)
        c_e = []
        for i in complication_elements:
            c_e.append(i.id)
        allowance_discount = mommy.make('atelier.AllowanceDiscount', _quantity=3)
        a_d = []
        for j in allowance_discount:
            a_d.append(j.id)
        now = datetime.datetime.now().date()
        response = self.client.post(
            reverse_lazy('atelier:order_update_form', kwargs={'pk': order.id}),
            data={
                'client': my_client.id,
                'product': product.id,
                'fabric': fabric.id,
                'processing_category': 1,
                'complication_elements': c_e,
                'allowance_discount': a_d,
                'order_date': now,
                'performer': self.user.id,
                'deadline': now + datetime.timedelta(weeks=2),
                'is_closed': False,
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/order/{}/'.format(order.id))
        order.refresh_from_db()
        self.assertEqual(order.client, my_client)
        self.assertEqual(order.product, product)
        self.assertEqual(order.fabric, fabric)
        self.assertEqual(order.processing_category, '1')
        self.assertTrue(order.complication_elements)
        self.assertTrue(order.allowance_discount)
        self.assertEqual(order.order_date, now)
        self.assertEqual(order.performer, self.user)
        self.assertEqual(order.deadline, now + datetime.timedelta(weeks=2))
        self.assertEqual(order.is_closed, False)
        self.assertEqual(Order.objects.get(id=order.id).last_updated_by, self.tailor)


class OrderDeleteViewTests(SetUpPreMixin):
    def test_order_delete_view_no_logged_in(self):
        instance = mommy.make('atelier.Order')
        response = self.client.get('/en/atelier/order/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_order_delete_view_not_tailor(self):
        self.client.login(username='user', password='userpassword')
        instance = mommy.make('atelier.Order', atelier=self.user.profile.atelier)
        response = self.client.get('/en/atelier/order/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_order_delete_view_tailor_not_in_atelier(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Order')
        response = self.client.get('/en/atelier/order/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_order_delete_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Order', atelier=self.tailor.profile.atelier)
        self.assertEqual(Order.objects.count(), 1)
        response = self.client.post('/en/atelier/order/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/order/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/order/')
        self.assertEqual(Order.objects.count(), 0)

    def test_order_delete_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.Order', atelier=self.atelier)
        self.assertEqual(Order.objects.count(), 1)
        response = self.client.post('/en/atelier/order/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/order/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/order/')
        self.assertEqual(Order.objects.count(), 0)


class OrderListViewTests(SetUpPreMixin):

    def test_order_list_view_no_logged_in(self):
        response = self.client.get('/en/atelier/order/')
        self.assertEqual(response.status_code, 302)
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_order_list_view_user(self):
        '''
        test: user can see orders of his atelier only
        '''
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Order', atelier=self.user.profile.atelier, _quantity=2)
        mommy.make('atelier.Order', _quantity=4)
        response = self.client.get('/en/atelier/order/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/order_list.html')
        self.assertEqual(len(response.context['object_list']), 2)

    def test_order_list_pagination_is_ten(self):
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Order', atelier=self.user.profile.atelier,
                   _quantity=13)  # Create an instances more than 10 for pagination tests (13 instances)
        resp = self.client.get(reverse_lazy('atelier:order_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 10)

    def test_order_list_all_elements(self):
        # get second page and confirm it has (exactly) remaining 3 items
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Order', atelier=self.user.profile.atelier,
                   _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:order_list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 3)

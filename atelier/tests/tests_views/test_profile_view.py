import htmls
from django.contrib.auth.models import User
from model_mommy import mommy
from atelier.models import Profile
from django.urls import reverse_lazy
from atelier.tests.tests_views.setup_premixin import SetUpPreMixin


class ProfileDetaileViewTests(SetUpPreMixin):

    def test_profile_detail_view_not_logged_in(self):
        item = mommy.make('atelier.Profile')
        response = self.client.get(reverse_lazy('atelier:profile_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 404)

    def test_profile_detail_view_user(self):
        self.client.login(username='user', password='userpassword')
        item = mommy.make('atelier.Profile', atelier=self.user.profile.atelier)
        response = self.client.get(reverse_lazy('atelier:profile_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 404)

    def test_profile_detail_view_tailor_not_this_atelier(self):
        self.client.login(username='tailor', password='tailorpassword')
        item = mommy.make('atelier.Profile')
        response = self.client.get(reverse_lazy('atelier:profile_detail', kwargs={'pk': item.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 404)

    def test_profile_detail_view_tailor(self):
        '''
        test by the help of htmls module. (see https://github.com/espenak/htmls/)
        '''
        user_2 = mommy.make('User')
        self.client.login(username='tailor', password='tailorpassword')
        kwargs = {
            'id': 1,
            'user': user_2,
            'is_tailor': False,
            'atelier': self.tailor.profile.atelier,
        }
        instance = mommy.make('atelier.Profile', **kwargs)
        response = self.client.get('/en/atelier/profile/{}/'.format(instance.id))
        self.assertEqual(response.status_code, 200)
        selector = htmls.S(response.content)
        user = selector.one('.user').alltext_normalized
        atel = selector.one('.atelier').alltext_normalized
        is_tailor = selector.one('.is_tailor').alltext_normalized
        self.assertEqual(user, user_2.username)
        self.assertEqual(atel, self.tailor.profile.atelier.name)
        self.assertEqual(is_tailor, 'simple profile')
        self.assertTemplateUsed(response, 'atelier/profile_detail.html')

    def test_profile_detail_view_superuser(self):
        '''
        test by the help of htmls module. (see https://github.com/espenak/htmls/)
        '''
        user_2 = mommy.make('User')
        self.client.login(username='superuser', password='supassword')
        kwargs = {
            'id': 1,
            'user': user_2,
            'is_tailor': False,
            'atelier': self.superuser.profile.atelier,
        }
        instance = mommy.make('atelier.Profile', **kwargs)
        response = self.client.get('/en/atelier/profile/{}/'.format(instance.id))
        selector = htmls.S(response.content)
        user = selector.one('.user').alltext_normalized
        atel = selector.one('.atelier').alltext_normalized
        is_tailor = selector.one('.is_tailor').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user, user_2.username)
        self.assertEqual(atel, self.tailor.profile.atelier.name)
        self.assertEqual(is_tailor, 'simple profile')
        self.assertTemplateUsed(response, 'atelier/profile_detail.html')


class ProfileCreateViewTests(SetUpPreMixin):

    def test_profile_create_view_not_logged_in(self):
        response = self.client.post(reverse_lazy('atelier:profile_form'))
        self.assertEqual(response.status_code, 404)

    def test_client_create_view_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.post(reverse_lazy('atelier:profile_form'))
        self.assertEqual(response.status_code, 404)

    def test_profile_create_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        response = self.client.post(reverse_lazy('atelier:profile_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')

    def test_profile_create_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        response = self.client.post(reverse_lazy('atelier:profile_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/create_form.html')


class ProfileEditViewTests(SetUpPreMixin):

    def test_profile_edit_view_not_logged_in(self):
        instance = mommy.make('atelier.Profile')
        response = self.client.post(reverse_lazy('atelier:profile_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_profile_edit_view_user(self):
        self.client.login(username='user', password='userpassword')
        instance = mommy.make('atelier.Profile', atelier=self.user.profile.atelier)
        response = self.client.post(reverse_lazy('atelier:profile_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_profile_edit_view_tailor_not_in_atelier(self):
        instance = mommy.make('atelier.Profile')
        tailor_user = User.objects.create_user('tuser', 'tailor@thebeatles.com', 'tpassword')
        tailor_profile = mommy.make('atelier.Profile', user=tailor_user, is_tailor=True)
        self.client.login(username='tuser', password='tpassword')
        response = self.client.post(reverse_lazy('atelier:profile_update_form', kwargs={'pk': instance.id}))
        self.assertEqual(response.status_code, 404)

    def test_profile_edit_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Profile', atelier=self.tailor.profile.atelier)
        response = self.client.post(
            reverse_lazy('atelier:profile_update_form', kwargs={'pk': instance.id}),
            data={
                'email': 'Super@ukr.net',
                'is_tailor': False,
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/profile/')
        instance.refresh_from_db()
        self.assertEqual(instance.user.email, 'Super@ukr.net')
        self.assertEqual(instance.is_tailor, False)

    def test_profile_edit_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.Profile')
        response = self.client.post(
            reverse_lazy('atelier:profile_update_form', kwargs={'pk': instance.id}),
            data={
                'email': 'Super@ukr.net',
                'is_tailor': False,
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/profile/')
        instance.refresh_from_db()
        self.assertEqual(instance.user.email, 'Super@ukr.net')
        self.assertEqual(instance.is_tailor, False)


class ProfileDeleteViewTests(SetUpPreMixin):

    def test_profile_delete_view_no_logged_in(self):
        instance = mommy.make('atelier.Profile')
        response = self.client.get('/en/atelier/profile/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_profile_delete_view_tailor_not_in_atelier(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Profile')
        response = self.client.get('/en/atelier/profile/{}/delete/'.format(instance.id))
        self.assertEqual(response.status_code, 404)

    def test_profile_delete_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        instance = mommy.make('atelier.Profile', atelier=self.user.profile.atelier)
        self.assertEqual(Profile.objects.count(), 4)  # + 3 profile instances from SetUpPreMixin
        response = self.client.post('/en/atelier/profile/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/profile/')
        self.assertEqual(Profile.objects.count(), 3)

    def test_profile_delete_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        instance = mommy.make('atelier.Profile')
        self.assertEqual(Profile.objects.count(), 4)  # + 3 profile instances from SetUpPreMixin
        response = self.client.post('/en/atelier/profile/{}/delete/'.format(instance.id))
        self.assertRedirects(response, '/en/atelier/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/atelier/profile/')
        self.assertEqual(Profile.objects.count(), 3)


class ProfileListViewTests(SetUpPreMixin):

    def test_profile_list_view_no_logged_in(self):
        response = self.client.get('/en/atelier/profile/')
        self.assertEqual(response.status_code, 404)

    def test_profile_list_view_user(self):
        self.client.login(username='user', password='userpassword')
        mommy.make('atelier.Profile', atelier=self.user.profile.atelier)
        response = self.client.get('/en/atelier/profile/')
        self.assertEqual(response.status_code, 404)

    def test_profile_list_view_tailor(self):
        self.client.login(username='tailor', password='tailorpassword')
        mommy.make('atelier.Profile', atelier=self.tailor.profile.atelier, _quantity=2)  # this atelier profiles
        mommy.make('atelier.Profile', _quantity=10)  # not this atelier profiles (tailor has not see)
        response = self.client.get('/en/atelier/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/profile_list.html')
        self.assertEqual(len(response.context['object_list']), 5)  # + 3 profile instances from SetUpPreMixin

    def test_profile_list_view_superuser(self):
        self.client.login(username='superuser', password='supassword')
        mommy.make('atelier.Profile', atelier=self.superuser.profile.atelier, _quantity=3)
        response = self.client.get('/en/atelier/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atelier/profile_list.html')
        self.assertEqual(len(response.context['object_list']), 6)  # + 3 profile instances from SetUpPreMixin

    def test_profile_pagination_is_ten(self):
        self.client.login(username='superuser', password='supassword')
        # Create an instances more than 10 for pagination tests (13 instances)
        mommy.make('atelier.Profile', _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:profile_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 10)

    def test_profile_list_all_elements(self):
        # get second page and confirm it has (exactly) remaining 3 items
        self.client.login(username='superuser', password='supassword')
        mommy.make('atelier.Profile', _quantity=13)
        resp = self.client.get(reverse_lazy('atelier:profile_list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['object_list']), 6)  # + 3 profile instances from SetUpPreMixin

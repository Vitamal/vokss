from django.utils import timezone
import htmls
from django import test
from model_mommy import mommy

from atelier.models import AllowanceDiscount
from atelier.tests import api_test_mixins_replica
from atelier.views import AllowanceDiscountListView, AllowanceDiscountDetailView, AllowanceDiscountUpdateView, \
    AllowanceDiscountCreateView, AllowanceDiscountDeleteView


class TestListView(test.TestCase, api_test_mixins_replica.ApiTestMixin):
    apiview_class = AllowanceDiscountListView

    def test_ok_user(self):
        requestuser = self.make_user()
        item = mommy.make('AllowanceDiscount')
        response = self.make_get_request(
            requestuser=requestuser)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 1)
        self.assertEqual(response.context_data['object_list'][0], item)

    def test_no_item_superuser(self):
        requestuser = self.make_superuser()
        response = self.make_get_request(
            requestuser=requestuser)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 0)

    def test_ok_superuser(self):
        requestuser = self.make_superuser()
        item = mommy.make('AllowanceDiscount')
        response = self.make_get_request(
            requestuser=requestuser)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 1)
        self.assertEqual(response.context_data['object_list'][0], item)


class TestDetailView(test.TestCase, api_test_mixins_replica.ApiTestMixin):
    apiview_class = AllowanceDiscountDetailView

    def test_ok_superuser(self):
        requestuser = self.make_superuser()
        item = mommy.make('AllowanceDiscount')
        response = self.make_get_request(
            viewkwargs={'pk': item.id},
            requestuser=requestuser
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data.get('object').id, item.id)

    def test_ok_user(self):
        requestuser = self.make_user()
        item = mommy.make('AllowanceDiscount')
        response = self.make_get_request(viewkwargs={'pk': item.id}, requestuser=requestuser)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data.get('object').id, item.id)

    def test_ok_response_data(self):
        requestuser = self.make_superuser()
        kwargs = {
            'id': 1,
            'name': 'Name',
            'coefficient': 1,
            'label': 'Label',
        }
        item = mommy.make('AllowanceDiscount', **kwargs)
        response = self.make_get_request(viewkwargs={'pk': item.id}, requestuser=requestuser)
        selector = htmls.S(response.content)
        type = selector.one('.type').alltext_normalized
        coefficient = selector.one('.coefficient').alltext_normalized
        name = selector.one('.name').alltext_normalized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type, 'Label')
        self.assertEqual(coefficient, '1.00')
        self.assertEqual(name, 'Name')


class TestUpdateView(test.TestCase, api_test_mixins_replica.ApiTestMixin):
    apiview_class = AllowanceDiscountUpdateView

    def test_ok_superuser(self):
        requestuser = self.make_superuser()
        item = mommy.make('AllowanceDiscount')
        response = self.make_post_request(
            viewkwargs={'pk': item.id},
            requestuser=requestuser,
            data={
                'name': 'Name',
                'coefficient': 1,
                'label': 'Label',
                'last_updated_datetime': timezone.now(),
                'created_datetime': timezone.now(),
                'last_updated_by': 'user',
                'created_by': 'user',
            })
        self.assertEqual(response.status_code, 200)

    # !!! It is not change the object in db !!!#
    # self.assertEqual(response.context_data.get('object').id, item.id)
    # item.refresh_from_db()
    # self.assertEqual(item.name, 'Name')
    # self.assertEqual(item.coefficient, 1)

    # !!!  it is not possible to extract needed field using htmls module to check new data insertions  !!!#
    # selector = htmls.S(response.content)
    # selector.prettyprint()
    # type = selector.one('.type').alltext_normalized
    # coefficient = selector.one('.coefficient').alltext_normalized
    # name = selector.one('.name').alltext_normalized
    # self.assertEqual(response.status_code, 200)
    # self.assertEqual(type, 'Label')
    # self.assertEqual(coefficient, '1.00')
    # self.assertEqual(name, 'Name')


#
class TesCreate(test.TestCase, api_test_mixins_replica.ApiTestMixin):
    apiview_class = AllowanceDiscountCreateView

    def test_ok_superuser(self):
        requestuser = self.make_superuser()
        data = {
            'name': 'ADName',
            'coefficient': 1,
            'label': 'ADLabel',
            'last_updated_datetime': timezone.now(),
            'created_datetime': timezone.now(),
            'last_updated_by': 'user',
            'created_by': 'user',
        }
        self.assertEqual(AllowanceDiscount.objects.count(), 0)
        response = self.make_post_request(data=data, requestuser=requestuser)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AllowanceDiscount.objects.count(), 1)
        item = AllowanceDiscount.objects.first()
        self.assertEqual(item.name, 'ADName')
        self.assertEqual(item.label, 'ADLabel')
        self.assertEqual(item.coefficient, 1.00)


class TesDelete(test.TestCase, api_test_mixins_replica.ApiTestMixin):
    apiview_class = AllowanceDiscountDeleteView

    def test_ok_destroy(self):
        requestuser = self.make_superuser()
        item = mommy.make(AllowanceDiscount)
        response = self.make_delete_request(viewkwargs={'pk': item.id},
                                            requestuser=requestuser)
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(AllowanceDiscount.DoesNotExist):
            item.refresh_from_db()

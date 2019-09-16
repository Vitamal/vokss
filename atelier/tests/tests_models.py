from django.test import TestCase


# Create your tests here.

from atelier.models import Client


class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(first_name='Big', last_name='Bob', tel_number='067-200-333-44', place='Stryi')

    def test_first_name_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first Name')

    def test_last_name_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'second Name')

    def test_place_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('place').verbose_name
        self.assertEquals(field_label, 'place')

    def test_tel_number_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('tel_number').verbose_name
        self.assertEquals(field_label, 'tel. number')

    def test_first_name_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)

    def test_tel_number_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('tel_number').max_length
        self.assertEquals(max_length, 30)

    def test_place_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('place').max_length
        self.assertEquals(max_length, 30)

    def test_object_name_is_first_name_last_name(self):
        client = Client.objects.get(id=1)
        expected_object_name = '%s %s' % (client.first_name, client.last_name)
        self.assertEquals(expected_object_name, str(client))

    def test_get_absolute_url(self):
        client = Client.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(client.get_absolute_url(), '/atelier/client/1/')



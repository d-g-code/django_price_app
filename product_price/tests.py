from django.test import TestCase
from .models import Store


class StoreModelTest(TestCase):

    def test_name_representation(self):
        # """max_length return False for name length 11 sign"""
        name_store = Store(store='abcdefghij')
        self.assertEqual(str(name_store), name_store.store)


class ProjectTest(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

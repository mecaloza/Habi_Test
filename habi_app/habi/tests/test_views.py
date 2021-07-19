from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse
from django.urls.base import clear_script_prefix
from habi.models import Property, Status, StatusHistory
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.search = reverse('search')

    def test_search_property_GET(self):
        response = self.client.get(self.search)
        self.assertEquals(response.status_code, 200)

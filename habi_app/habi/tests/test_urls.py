from django import urls
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from habi.views import Search_Property


class TestUrls(SimpleTestCase):

    def test_search_property_resolves(self):
        url = reverse("search")
        self.assertEquals(resolve(url).func.view_class, Search_Property)

from django.test import TestCase, Client
from django.urls import (reverse,
                         resolve)


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.main_url = reverse('')
        self.my_search_url = reverse('my-search/')
        self.aboutus_url = reverse('aboutus/')
        self.search_url = reverse('search')
        self.add_to_url = reverse('add-to-favourites/', args = 'element' )

    def test_main_GET(self):
        response = self.client.get(self.main_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_my_search_GET(self):
        response = self.client.get(self.my_search_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search.html')

    def test_about_us_GET(self):
        response = self.client.get(self.aboutus_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/aboutus.html')

    def test_search_GET(self):
        response = self.client.get(self.search_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search.html')

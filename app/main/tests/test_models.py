from django.test import TestCase, Client
from main.models import (Favourites,
                         Rating,
                         Search)


class TestSearchModels(TestCase):

    def setUP(self):
        self.search = Search.objects.create(
            search_word = "Deep Purple",
            result_url=  "https://www.youtube.com/watch?v=SMmDIMmQTak",
            filer = "views",
        )

    def test_search_is_slug_is_created_on_creation(self):
        self.assertEqual(self.search.slug, 'https://www.youtube.com/watch?v=SMmDIMmQTak+1')



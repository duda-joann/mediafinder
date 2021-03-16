from django.test import SimpleTestCase
from django.urls import (reverse,
                         resolve)
from main.views import (index,
                        search_movies,
                        return_search,
                        create_rating,
                        add_to_favourites,
                                        )


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('')
        self.assertEqual(resolve(url).func, index)

    def test_search_movies_url(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search_movies)

    def test_return_search(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, return_search)

    def test_create_rating_urls(self):
        url = reverse('aboutus')
        self.assertEqual(resolve(url).func, create_rating)

    def test_add_to_favourite_urls(self):
        url = reverse(r'add-to-favourites/<element>')
        self.assertEqual(resolve(url).func, add_to_favourites)

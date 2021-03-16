from django.urls import path
from .views import *


urlpatterns = [
    path('my-search/', return_search, name = "mysearch"),
    path('aboutus/', create_rating, name = "aboutus"),
    path('', index),
    path('search', search_movies, name="search"),
    path(r'add-to-favourites/<element>', add_to_favourites, name="favourite"),
    ]
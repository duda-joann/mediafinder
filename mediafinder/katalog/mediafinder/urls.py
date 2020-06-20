from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from .views import search_movies, register_new_user, return_search, create_rating


urlpatterns = [
    path('search/', search_movies, name="search"),
    path('registration/', register_new_user),
    path('my_search', return_search),
    path('aboutus', create_rating),
]
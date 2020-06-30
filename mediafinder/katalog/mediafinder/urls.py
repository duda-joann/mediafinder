from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib import admin
from .views import search_movies, register_new_user, return_search, create_rating, index, add_to_favourites

app_name = 'media'
urlpatterns = [
    path('search/', search_movies, name= "search"),
    path('registration/', register_new_user, name="register"),
    path('mysearch/', return_search, name = "mysearch"),
    path('aboutus/', create_rating, name = "aboutus"),
    re_path(r'^login/', include("django.contrib.auth.urls"), name="login"),
    path('', index),
    path('add/<str:video>', add_to_favourites, name = "addfavorites")
]
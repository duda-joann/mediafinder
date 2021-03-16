from django.urls import path, re_path
from django.conf.urls import include
from .views import register_new_user
from django.contrib import admin

app_name = 'accounts'

urlpatterns = [
    re_path(r'^registration/', register_new_user, name="register"),
    re_path(r'^login/', include("django.contrib.auth.urls"), name="login"),
    path('auth/', include('django.contrib.auth.urls')),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),

]
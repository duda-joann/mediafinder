from django import http
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from main.models import Favourites
from django.contrib import messages


@login_required()
def add_to_favourites(request: http.HttpRequest, slug :str) -> http.HttpResponse:
    video_url = request.GET.get('slug')
    favourite, created = Favourites.objects.get_or_create(user=request.user, video_url = video_url)
    user_favourites = Favourites.objects.filter(owner = request.user)
    if user_favourites:
        if user_favourites.filter(favourite.video_url == video_url):
            messages.info(request, "You have got video in your favourites")
            return redirect('app:mysearch')
        else:
            fav_attrs = {
                'user': request.user,
                'video_url': video_url
            }
            Favourites.objects.create(**fav_attrs)
            messages.success(request, "You added video successfully to favourites")
            return redirect('app:mysearch')

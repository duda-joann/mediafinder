from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .api import call_api
from .forms import FormSearch, RegisterForm, RatingForm
from .models import Search, Rating


# Create your views here.


def index(request: http.HttpRequest) -> http.HttpResponse:
    title = "MEDIA FINDER"
    return render(request, "main.html", {'title': title})


def register_new_user(request: http.HttpRequest) -> http.HttpResponse:
    form_register = RegisterForm(request.POST)
    if form_register.is_valid():
        form_register.save()
        return redirect('search', errorMessage=None, successMessage=None)
    else:
        return render(request, 'register.html', {'form': form_register})


def search_movies(request: http.HttpRequest) -> http.HttpResponse:
    """ Get video ID from APi number one"""
    if request.method == "POST":
        form_search = FormSearch(request.POST)

        if form_search.is_valid:
            search_word: str = request.POST['search_word']
            order: str = request.POST['filter']
            form_search.save()
            search_api = "https://www.googleapis.com/youtube/v3/search"
            search_params = {
                'part': 'snippet',
                'order': order,
                'q': search_word,
                'key': 'AIzaSyDq40TMB7TjYBzTgcwQHzU_EQouYvprDHs',
                'maxResults': 12,
                'type': 'video',
            }

            data = call_api(search_api, search_params)

            video_id_list = [data['items'][i]['id']['videoId'] for i in range(12)]

            video_url = {video_id: "https://www.youtube.com/embed/" + video_id
                         for video_id in video_id_list}

            return render(request, 'search.html', {
                'form_search': form_search,
                'word': search_word,
                'video': video_url})
    else:
        form_search = FormSearch(request.POST)

    return render(request, 'search.html', {'form_search': form_search})


@login_required()
def return_search(request: http.HttpRequest) -> http.HttpResponse:
    if User.is_authenticated:
        user_search_result = Search.objects.filter(user=request.user).order_by('search_date')
        return render(request, 'my_search.html', {'result': user_search_result})
    else:
        return redirect(request, 'login/')


def create_rating(request: http.HttpRequest) -> http.HttpResponse:
    """create view for rating webside"""
    form = RatingForm()
    if request.method == "POST":
        review = Rating.objects.all().order_by('date')
        if form.is_valid:
            rate = int(request.POST['rate'])
            review = request.POST['review']
            form.save()
            return render(request, 'aboutus.html', {'form': form})
    else:

        return render(request, 'aboutus.html', {'form': form})

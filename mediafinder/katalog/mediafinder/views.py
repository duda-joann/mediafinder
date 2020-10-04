from django import http
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect, get_list_or_404
from .api import call_api
from django.contrib.auth.models import User
from .forms import FormSearch, RegisterForm, RatingForm, FavoritesForm
from .models import Search, Rating, Favourites
from .exceptions import CallApiError



# Create your views here.


def index(request: http.HttpRequest) -> http.HttpResponse:
    """
    Render main page
    :param request:
    :return; view of main page
    """
    title = "MEDIA FINDER"
    return render(request, "main.html", {'title': title})



def register_new_user(request: http.HttpRequest) -> http.HttpResponse:
    form_register = RegisterForm(request.POST)
    if form_register.is_valid():
        form_register.save()
        return redirect('login',)
    else:
        return render(request, 'register.html', {'form': form_register})


def search_movies(request: http.HttpRequest) -> http.HttpResponse:
    """
    Get video ID from APi number one
    :param request
    :return generate view with youtube result  on requested by user search word
    and  order by choosen by user param: order

    """

    if request.method == "POST":
        form_search = FormSearch(request.POST)

        if form_search.is_valid:
            try:
                search_word: str = request.POST['search_word']
                order: str = request.POST['filter']
                search_api = "https://www.googleapis.com/youtube/v3/search"
                search_params = {
                    'part': 'snippet',
                    'order': order,
                    'q': search_word,
                    'key': 'AIzaSyAaJPWwerdkyWGIfxL6oIMiJOkl1DCD6Lw',
                    'maxResults': 12,
                    'type': 'video',
                }

                data = call_api(search_api, search_params)

                video_id_list = [data['items'][i]['id']['videoId'] for i in range(12)]

                video_url = {video_id: "https://www.youtube.com/embed/" + video_id
                             for video_id in video_id_list}


                lines = []
                for key, value in video_url.items():
                    if request.user is None:
                        search_attrs = {
                        'user': request.user.username,
                        'search_word': search_word,
                        'result_url': value,
                        'filter': order,
                        }
                        Search.objects.create(**search_attrs)
                    else:
                        search_attrs = {
                            'search_word': search_word,
                            'result_url': value,
                            'filter': order,
                        }
                        Search.objects.create(**search_attrs)

            except CallApiError:
                return render(request, 'error.html')

            return render(request, 'search.html', {'video':video_url,
                                                   'form_search':form_search})

    else:
        form_search = FormSearch(request.POST)
        return render(request, "search.html", {'form_search':form_search})


@login_required()
def return_search(request: http.HttpRequest) -> http.HttpResponse:
    """
    Create view of last searches for logged users
    :param request:
    :return: generate page contains  result of search for logged users
    """
    if User.is_authenticated:
        user_search_result = Search.objects.filter(user = request.user)
        return render(request, 'my_search.html', {'result': user_search_result})


def create_rating(request: http.HttpRequest) -> http.HttpResponse:
    """create view for rating webside
    :param request:
    :return: generate viev of rating webside with form to rate for
    signup user and show  reviews orders by date for all users
    """
    review = Rating.objects.all().order_by('date')
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingForm()
        return render(request, 'aboutus.html', {'form': form,
                                                'review': review})


def add_to_favourites(request: http.HttpRequest) -> http.HttpResponse:
    fav = request.GET.get('video', '')
    owner = request.user
    Favourites.save()

    return render(request, 'add_to_fav.html', {'fav': fav})



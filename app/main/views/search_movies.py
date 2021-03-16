import os
from django import http
from django.shortcuts import render
from main.api import call_api
from main.forms import FormSearch
from main.models import Search
from main.exceptions import CallApiError


def search_movies(request: http.HttpRequest) -> http.HttpResponse:
    """
    Get video ID from APi number one and save result to database
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
                    'key': os.environ['API_KEY'],
                    'maxResults': 12,
                    'type': 'video',
                }

                data = call_api(search_api, search_params)

                video_id_list = [data['items'][i]['id']['videoId'] for i in range(12)]

                video_url = {video_id: "https://www.youtube.com/embed/" + video_id
                             for video_id in video_id_list}

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

            return render(request, 'main/search.html', {'video':video_url,
                                                   'form_search':form_search})

    else:
        form_search = FormSearch(request.POST)
        return render(request, "main/search.html", {'form_search':form_search})
from django import http
from django.shortcuts import render


# Create your views here.


def index(request: http.HttpRequest) -> http.HttpResponse:
    """
    Render main page
    :param request:
    :return; view of main page
    """
    title = "YOUTUBE MEDIA FINDER"
    return render(request, "main/main.html", {'title': title})
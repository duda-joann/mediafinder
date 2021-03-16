from django import http
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import Search


@login_required()
def return_search(request: http.HttpRequest) -> http.HttpResponse:
    """
    Create view of last searches for logged users
    :param request:
    :return: generate page contains  result of search for logged users
    """
    if User.is_authenticated:
        user_search_result = Search.search_by_user.all()
        return render(request, 'main/my_search.html', {'result': user_search_result})
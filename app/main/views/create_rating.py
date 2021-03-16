from django import http
from django.shortcuts import render, HttpResponseRedirect
from main.forms import RatingForm
from main.models import Rating


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
        return render(request, 'main/aboutus.html', {'form': form,
                                                'review': review})

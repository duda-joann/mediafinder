from django import http
from django.shortcuts import render, redirect
from .forms.register_form import UserRegisterForm

# Create your views here.


def register_new_user(request: http.HttpRequest) -> http.HttpResponse:
    form_register = UserRegisterForm(request.POST)
    if form_register.is_valid():
        form_register.save()
        return redirect('login')

    return render(request, 'register.html', {'form': form_register})



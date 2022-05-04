from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


def home(request):
    return redirect(to=reverse('index'))


def index(request):
    return HttpResponse('Страница приложения women.')


def categories(request, cat_id):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Статьи</h1><p>{cat_id}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

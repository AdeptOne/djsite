from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse

from . import services


MENU = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_article'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    template_name = 'women/index.html'

    articles = services.get_all_articles()
    categories = services.get_all_categories()

    context = {
        'menu': MENU,
        'articles': articles,
        'title': 'Главная страница',
        'categories': categories,
        'category_selected': 0
    }

    return render(request, template_name, context)


def about(request):
    template_name = 'women/about.html'
    context = {
        'title': 'О сайте',
    }

    return render(request, template_name, context)


def add_article(request):
    return HttpResponse("Add article")


def login(request):
    return HttpResponse("Login")


def contact(request):
    return HttpResponse("Contact")


def show_article(request, article_id):
    return HttpResponse("article")


def show_category(request, category_id):
    template_name = 'women/index.html'

    articles = services.get_articles_by_category(category_id)
    categories = services.get_all_categories()

    if len(articles) == 0:
        raise Http404()

    context = {
        'menu': MENU,
        'articles': articles,
        'title': 'Главная страница',
        'categories': categories,
        'category_selected': category_id
    }

    return render(request, template_name, context)


# def categories(request, cat_id):
#     if request.GET:
#         print(request.GET)
#
#     return HttpResponse(f"<h1>Статьи</h1><p>{cat_id}</p>")
#
#
# def archive(request, year):
#     return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

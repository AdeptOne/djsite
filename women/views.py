from django.http import Http404, HttpResponse
from django.shortcuts import render

from .forms import AddArticleForm
from .services import (get_all_articles, get_article_or_404_by_article_slug,
                       get_articles_by_category_slug, get_id_category_by_slug)


def index(request):
    articles = get_all_articles()

    context = {
        'articles': articles,
        'title': 'Главная страница',
        'category_selected': 0
    }

    return render(request, 'women/index.html', context)


def about(request):
    context = {
        'title': 'О сайте',
    }

    return render(request, 'women/about.html', context)


def add_article(request):
    form = AddArticleForm()

    context = {
        'title': 'Добавление статьи',
        'form': form,
    }

    return render(request, 'women/add_article.html', context)


def login(request):
    return HttpResponse("Login")


def contact(request):
    return HttpResponse("Contact")


def show_article(request, article_slug):
    article = get_article_or_404_by_article_slug(article_slug)

    context = {
        'article': article,
        'title': article.title,
        'category_selected': article.category_id,
    }

    return render(request, 'women/article.html', context)


def show_category(request, category_slug):
    articles = get_articles_by_category_slug(category_slug)
    id_selected_category = get_id_category_by_slug(category_slug)

    if len(articles) == 0:
        raise Http404()

    context = {
        'articles': articles,
        'title': 'Главная страница',
        'category_selected': id_selected_category
    }

    return render(request, 'women/index.html', context)


# def categories(request, cat_id):
#     if request.GET:
#         print(request.GET)
#
#     return HttpResponse(f"<h1>Статьи</h1><p>{cat_id}</p>")
#
#
# def archive(request, year):
#     return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

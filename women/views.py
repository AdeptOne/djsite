from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import AddArticleForm
from .models import Article
from .services import (get_all_articles, get_category_name_by_slug,
                       get_id_category_by_slug)


class ArticleHome(ListView):
    template_name = 'women/index.html'

    queryset = get_all_articles().filter(is_published=True)
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['category_selected'] = 0
        return context


def about(request):
    context = {
        'title': 'О сайте',
    }

    return render(request, 'women/about.html', context)


class AddArticle(CreateView):
    form_class = AddArticleForm
    template_name = 'women/add_article.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


def login(request):
    return HttpResponse("Login")


def contact(request):
    return HttpResponse("Contact")


class ShowArticle(DetailView):
    model = Article
    template_name = 'women/article.html'
    slug_url_kwarg = 'article_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['article']
        return context


class ArticleCategoryList(ListView):
    model = Article
    template_name = 'women/index.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_selected'] = get_id_category_by_slug(self.kwargs['category_slug'])
        context['title'] = 'Категория: ' + get_category_name_by_slug(self.kwargs['category_slug'])
        return context


# def index(request):
#     articles = get_all_articles()
#
#     context = {
#         'articles': articles,
#         'title': 'Главная страница',
#         'category_selected': 0
#     }
#
#     return render(request, 'women/index.html', context)

# def add_article(request):
#     if request.method == 'POST':
#         form = AddArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddArticleForm()
#
#     context = {
#         'title': 'Добавление статьи',
#         'form': form,
#     }
#
#     return render(request, 'women/add_article.html', context)

# def show_article(request, article_slug):
#     article = get_article_or_404_by_article_slug(article_slug)
#
#     context = {
#         'article': article,
#         'title': article.title,
#         'category_selected': article.category_id,
#     }
#
#     return render(request, 'women/article.html', context)


# def show_category(request, category_slug):
#     articles = get_articles_by_category_slug(category_slug)
#     id_selected_category = get_id_category_by_slug(category_slug)
#
#     if len(articles) == 0:
#         raise Http404()
#
#     context = {
#         'articles': articles,
#         'title': 'Главная страница',
#         'category_selected': id_selected_category
#     }
#
#     return render(request, 'women/index.html', context)


# def categories(request, cat_id):
#     if request.GET:
#         print(request.GET)
#
#     return HttpResponse(f"<h1>Статьи</h1><p>{cat_id}</p>")
#
#
# def archive(request, year):
#     return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

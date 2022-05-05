from django.urls import path, re_path

from women.views import (about, add_article, contact, index, login,
                         show_article, show_category)

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('add-article/', add_article, name='add_article'),
    path('article/<slug:article_slug>/', show_article, name='article'),
    path('category/<slug:category_slug>/', show_category, name='category')
    # re_path(r'^archive/(?P<year>\d{4})/', archive),
    # path('cats/<int:cat_id>/', categories),
]

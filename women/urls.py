from django.urls import path, re_path

from women.views import (AddArticle, ArticleCategoryList, ArticleHome,
                         ShowArticle, about, contact, login)

urlpatterns = [
    path('', ArticleHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('add-article/', AddArticle.as_view(), name='add_article'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    path('category/<slug:category_slug>/', ArticleCategoryList.as_view(), name='category')
    # re_path(r'^archive/(?P<year>\d{4})/', archive),
    # path('cats/<int:cat_id>/', categories),
]

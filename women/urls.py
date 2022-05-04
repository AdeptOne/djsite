from django.urls import path, re_path

from women.views import index, about, contact, login, add_article, show_article, show_category

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('add-article/', add_article, name='add_article'),
    path('article/<int:article_id>/', show_article, name='article'),
    path('category/<int:category_id>/', show_category, name='category')
    # re_path(r'^archive/(?P<year>\d{4})/', archive),
    # path('cats/<int:cat_id>/', categories),
]

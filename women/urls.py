from django.urls import path, re_path

from women.views import index, categories, archive

urlpatterns = [
    path('', index),
    path('cats/<int:cat_id>/', categories),
    re_path(r'^archive/(?P<year>\d{4})/', archive),
]

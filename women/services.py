from typing import Union

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Article, Category


def get_all_articles() -> QuerySet[Article]:
    return Article.objects.all()


def get_article_or_404_by_article_slug(article_slug: str) -> Union[Article, Http404]:
    return get_object_or_404(Article, slug=article_slug)


def get_articles_by_category_slug(category_slug: str) -> QuerySet[Article]:
    return Article.objects.filter(category__slug=category_slug)


def get_id_category_by_slug(category_slug: str) -> int:
    try:
        category_id = Category.objects.get(slug=category_slug).id
        return category_id
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist('Категории с таким слагом не существует')


def get_category_name_by_slug(category_slug: str) -> str:
    try:
        category_name = Category.objects.get(slug=category_slug).name
        return category_name
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist('Категории с таким слагом не существует')


def get_all_categories() -> QuerySet[Category]:
    return Category.objects.all()


def get_categories_sorted_by(sort_option: str) -> QuerySet[Category]:
    return Category.objects.order_by(sort_option)


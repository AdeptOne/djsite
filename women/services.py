from django.db.models import QuerySet

from .models import Article, Category


def get_all_articles() -> Article:
    return Article.objects.all()


def get_all_categories() -> Category:
    return Category.objects.all()


def get_articles_by_category(category_id: int) -> Article:
    return Article.objects.filter(category_id=category_id)


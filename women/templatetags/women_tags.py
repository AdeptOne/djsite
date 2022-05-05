from django import template

from women import services

register = template.Library()

register.simple_tag(services.get_all_categories,
                    name='get_all_categories')


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort_option: str = None, category_selected: int = 0):
    """
    Отображает список категорий, который может быть отсортирован.
    Так-же указывает выбранную категорию.

    :param sort_option: может быть одним из ('name', 'pk')
    :param category_selected: принимает номер выбранной категории
    """
    categories = services.get_all_categories() if not sort_option\
        else services.get_categories_sorted_by(sort_option)

    context = {
        'categories': categories,
        'category_selected': category_selected,
    }

    return context


@register.inclusion_tag('women/menu_list.html')
def show_menu():
    '''Отображает навигационное меню сайта.'''
    menu = [
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_article'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
    ]

    context = {
        'menu': menu
    }

    return context

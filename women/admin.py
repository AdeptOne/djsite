from django.contrib import admin

from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    list_max_show_all = 15
    search_fields = ('title', 'content')
    list_editable = 'is_published',
    list_filter = ('is_published', 'created_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = 'name',


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

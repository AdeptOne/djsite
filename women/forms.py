from django import forms

from .models import Article, Category
from .services import get_all_categories


class AddArticleForm(forms.Form):
    categories = get_all_categories()

    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=categories)

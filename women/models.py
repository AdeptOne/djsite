from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    content = models.TextField('Текст статьи', blank=True)
    photo = models.ImageField('Фото', upload_to="photos/%Y/%m/%d/")
    created_at = models.DateTimeField('Время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Время изменения', auto_now=True)
    is_published = models.BooleanField('Публикация', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'Название статьи: {self.title}'

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.pk})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'

        ordering = ['-created_at', 'title']


class Category(models.Model):
    name = models.CharField('категория', max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

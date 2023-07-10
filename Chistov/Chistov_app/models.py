from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=11, verbose_name="Телефон")
    message = models.TextField(max_length=200, verbose_name="Сообщение")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время отправки сообщения", )

    def __str__(self):
        return self.name

    # класс для изменения названия таблицы в админке
    class Meta:
        verbose_name = 'Входящий контакт'
        verbose_name_plural = 'Входящие контакты'
        ordering = ['-time_create']  # сортировка записей


class Reviews(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя клиента:")
    reviews = models.TextField(max_length=500, verbose_name="Отзыв клиента")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания отзыва")

    def __str__(self):
        return self.name

    # класс для изменения названия таблицы в админке
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-time_create',)  # сортировка записей


class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name="Название фотосессии")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    # класс для изменения названия таблицы в админке
    class Meta:
        verbose_name = 'Категория фотосессии'
        verbose_name_plural = 'Категории фотосессии'
        ordering = ['name_category']  # сортировка записей

    def __str__(self):
        return self.name_category

    def get_absolute_url(self):
        return reverse('show_media', kwargs={'slug_cat': self.slug})


class Media(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категории фотосессии")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")
    video = EmbedVideoField(blank=True, verbose_name='Видео')
    time_create = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    # класс для изменения названия таблицы в админке
    class Meta:
        verbose_name = 'Фото, видео'
        verbose_name_plural = 'Фото, видео'
        ordering = ('-time_create',)  # сортировка записей



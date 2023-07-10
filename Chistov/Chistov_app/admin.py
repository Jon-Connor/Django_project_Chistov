from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


# Регистрация таблиц в админке
# admin.site.register(Contact, ContactAdmin) - 1 способ
# Таблица контакты
@admin.register(Contact)  # 2 способ
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message', 'time_create')  # для добавления полей в админку
    list_display_links = ('id', 'name', 'phone', 'message')  # для добавления полей в админку, как ссылки
    search_fields = ('id', 'name', 'time_create')  # для поиска по полям
    list_editable = ()  # для обозначения редактируемых полей
    list_filter = ('time_create',)  # для фильтрации (по каким полям фильтровать данные)


# Таблица отзывы
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'reviews', 'time_create')  # для добавления полей в админку
    list_display_links = ('name', 'reviews')  # # для добавления полей в админку, как ссылки
    search_fields = ('name', 'reviews')  # для поиска по полям
    list_editable = ()  # для обозначения редактируемых полей
    list_filter = ('time_create',)  # для фильтрации (по каким полям фильтровать данные)


# Таблица с медиа
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'get_foto', 'video', 'time_create')  # для добавления полей в админку
    list_display_links = ('get_foto', 'video')  # для добавления полей в админку, как ссылки
    search_fields = ('id',)  # для поиска по полям
    list_editable = ()  # для обозначения редактируемых полей
    list_filter = ('time_create', 'cat')  # для фильтрации (по каким полям фильтровать данные)
    fields = ('cat', 'photo', 'get_foto', 'video', 'time_create')
    readonly_fields = ('time_create', 'get_foto')

    def get_foto(self, object):  # метод для отображения фото в админке
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=150>")

    # для изменения заголовка поля
    get_foto.short_description = "Фото"


# Таблица категорий
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')  # для добавления полей в админку
    list_display_links = ('id', 'name_category')  # # для добавления полей в админку, как ссылки
    search_fields = ('id', 'name_category')  # для поиска по полям
    list_editable = ()  # для обозначения редактируемых полей
    list_filter = ()  # для фильтрации (по каким полям фильтровать данные)
    prepopulated_fields = {'slug': ('name_category',)}  # создавать слаг на основе названия категории

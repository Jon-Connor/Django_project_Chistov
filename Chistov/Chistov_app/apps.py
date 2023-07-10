from django.apps import AppConfig


class ChistovAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Chistov_app'
    verbose_name = 'Мой сайт'  # изменят имя приложения в админке

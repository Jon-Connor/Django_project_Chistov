from django.contrib.auth import logout, login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from Chistov_app.forms import *
from Chistov_app.models import *
from django.urls import reverse_lazy, reverse

# Данные контактов и иконок соц.сетей(ссылки и изображение)
contact_data = {"data_icon": [{'url': 'https://vk.com/pasha4istov', 'icon': 'img/vk.png'},
                              {'url': 'https://www.instagram.com/pasha4istov/', 'icon': 'img/inst.png'},
                              {'url': 'https://t.me/pasha4istov', 'icon': 'img/tlg.png'}],
                "phone": "+375(29)150-56-73"}


# главная страница
def index(request):
    context = {'contact_data': contact_data, "title": "Главная страница"}
    return render(request, 'index.html', context=context)


# страница портфолио
class Portfolio(ListView):
    model = Category
    template_name = 'portfolio.html'
    context_object_name = 'data_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Портфолио"
        context['contact_data'] = contact_data
        return context


# страница показа фото
class ShowMedia(ListView):
    model = Media
    template_name = 'show_media.html'
    context_object_name = 'media'

    def get_queryset(self):
        return Media.objects.filter(cat__slug=self.kwargs['slug_cat'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Фото"
        context['contact_data'] = contact_data
        return context


# страница с ценами
def prices(request):
    context = {'contact_data': contact_data, 'title': 'Цены'}
    return render(request, 'prices.html', context=context)


# страница отзывы
class Review(ListView):
    model = Reviews
    form = ReviewsForm
    template_name = 'reviews.html'
    context_object_name = 'reviews_user'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context["title"] = "Отзывы"
        context['contact_data'] = contact_data
        return context

    def post(self, request, *args, **kwargs):
        reviews_user = self.model.objects.all()[:5]
        context = {'contact_data': contact_data, 'title': "Отзывы",
                   'reviews_user': reviews_user, }
        data_form = ReviewsForm(request.POST)  # данные из формы
        if data_form.is_valid():
            data_form.save()
        return render(request, 'reviews.html', context=context)


# страница с контактами
class Contacts(CreateView):
    form_class = ContactForm
    template_name = 'contacts.html'

    # extra_context = {"telephone": "telephone"}  # пример

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_data'] = contact_data
        context['title'] = 'Контакты'
        return context

    def post(self, request, *args, **kwargs):
        context = {'contact_data': contact_data, 'title': 'Контакты'}
        data_form = ContactForm(request.POST)  # данные из формы
        if data_form.is_valid():
            data_form.save()
        return render(request, 'contacts.html', context=context)


# страница регистрации пользователя сайта
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "registration.html"

    # success_url = reverse_lazy("home")
    # перенаправление при успешной регистрации, если не использовать метод(form_valid)

    # Метод для проверки и сохранения введенных данных в форму
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_data'] = contact_data
        return context


# страница авторизации
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "authorization.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_data'] = contact_data
        return context

    # метод, перевода на url адрес(страницы) при успешной авторизации
    def get_success_url(self):
        return reverse_lazy("home")


# метод для выхода из авторизации
def logout_user(request):
    logout(request)
    return redirect("authorization")

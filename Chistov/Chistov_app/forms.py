from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import *


# Форма контакты
class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Ваше имя:",
                           widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Ваше имя:"}))
    phone = forms.CharField(label="ваш телефон:",
                            widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Ваш телефон:"}))
    message = forms.CharField(label="Ваше сообщение:",
                              widget=forms.Textarea(attrs={'class': "form-control", "style": "height: 150px",
                                                           'placeholder': "Ваше сообщение:"}))

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['message'].widget.attrs.update({'class': 'special'})

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Ваше имя:"}),
        #     'phone': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Ваш телефон:"}),
        #     'message': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Ваше сообщение:"}),
        # }


# Форма отзывы
class ReviewsForm(forms.ModelForm):
    name = forms.CharField(label="Ваше имя:",
                           widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Ваше имя:"}))
    reviews = forms.CharField(label="Ваш отзыв:",
                              widget=forms.Textarea(attrs={'class': "form-control", "style": "height: 200px",
                                                           'placeholder': "Ваш Отзыв:"}))

    class Meta:
        model = Reviews
        fields = ['name', 'reviews']


# Форма регистрации
class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Ваше имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше имя:"}))
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Логин:"}))
    password1 = forms.CharField(label="Пароль",
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Пароль:"}))
    password2 = forms.CharField(label="Повтор пароля",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': "Повтор пароля:"}))
    captcha = CaptchaField(help_text='Введите символы с картинки')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2', 'captcha']


# Форма входа
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Логин:"}))
    password = forms.CharField(label="пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Пароль:"}))

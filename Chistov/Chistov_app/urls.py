from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', index, name='home'),
    path('portfolio', (cache_page(300))(Portfolio.as_view()), name='portfolio'),
    path('portfolio/<slug:slug_cat>', ShowMedia.as_view(), name='show_media'),
    path('prices', prices, name='prices'),
    path('reviews', Review.as_view(), name='reviews'),
    path('contacts', Contacts.as_view(), name='contacts'),
    path('registration', RegisterUser.as_view(), name='registration'),
    path('authorization', LoginUser.as_view(), name='authorization'),
    path('logout', logout_user, name='logout'),
]

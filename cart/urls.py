from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', cartView, name='cart'),
    path('cart/<id>', add_to_cart, name='cart'),

]

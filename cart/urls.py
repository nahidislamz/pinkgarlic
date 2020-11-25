from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', cartView, name='cart'),
    path('<id>', add_to_cart, name='cart'),
    path('increaseItem/<id>', increaseItem, name='increaseItem'),
    path('decreaseItem/<id>', decreaseItem, name='decreaseItem'),
    path('remove/<id>', removeCart, name='removecart'),

]

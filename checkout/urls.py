from django.urls import path
from .views import *


urlpatterns = [
    path('checkout/', checkout, name="checkout"),
    path('payment/', payment, name="payment"),
    path('charge/', charge, name="charge"),
    path('orders/', oderView, name="orders"),
]

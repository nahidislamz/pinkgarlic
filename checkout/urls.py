from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('checkout/', checkout, name="checkout"),
    path('payment/', payment, name="payment"),
    path('charge/', charge, name="charge"),
    path('orders/', oderView, name="orders"),
]

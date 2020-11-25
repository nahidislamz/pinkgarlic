from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('checkout/', checkout, name="checkout"),
    path('payment/', payment, name="payment"),
    path('charge/', charge, name="charge"),
    path('orders/', orderView, name="orders"),
    path('address/<int:id>', address_form, name="address_update")
]

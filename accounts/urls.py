from django.urls import path
from accounts.views import (registerPage, loginPage, logoutPage, profilePage)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),
    path('profile/', profilePage, name="profile"),
]

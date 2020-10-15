from django.shortcuts import render
from .models import Menu
# Create your views here.


def menuPage(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menus': menus})

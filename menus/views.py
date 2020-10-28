from django.shortcuts import render
from .models import Menu, Category
# Create your views here.


def menuPage(request):
    category = Category.objects.all()
    menus = Menu.objects.all()
    context = {
        'menus': menus,
        'category': category
    }
    return render(request, 'menu.html', context)

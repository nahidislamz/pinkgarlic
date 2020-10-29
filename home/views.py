from django.shortcuts import render
from menus.models import Menu, Category

# Create your views here.


def homeView(request):
    category = Category.objects.all()
    menus = Menu.objects.all()
    context = {
        'menus': menus,
        'category': category
    }
    return render(request, 'index.html', context)

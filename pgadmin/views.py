from django.shortcuts import render, redirect
from menus.models import Menu, Category
from accounts.models import Customer
from cart.models import Order
from .forms import *
# Create your views here.


def adminView(request):
    return render(request, 'dashboard.html')


def menuAdminView(request):
    menu = Menu.objects.all()
    return render(request, 'menu/menu_admin.html', {'menu': menu})


def menu_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MenuForm()
        else:
            menu = Menu.objects.get(id=id)
            form = MenuForm(instance=menu)
        return render(request, "menu/menu_form.html", {'form': form})
    else:
        if id == 0:
            form = MenuForm(request.POST)
        else:
            menu = Menu.objects.get(id=id)
            form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
        return redirect('menuadmin')


def menu_delete(request, id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    return redirect('categoryadmin')


def categoryView(request):
    category = Category.objects.all()
    return render(request, 'category/category_admin.html', {'category': category})


def category_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CategoryForm()
        else:
            category = Category.objects.get(id=id)
            form = CategoryForm(instance=category)
        return render(request, "category/category_form.html", {'form': form})
    else:
        if id == 0:
            form = CategoryForm(request.POST)
        else:
            category = Category.objects.get(id=id)
            form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('categoryadmin')


def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('categoryadmin')


def customerView(request):
    customer = Customer.objects.all()
    return render(request, 'accounts/customers.html', {'customer': customer})


def orderViewAdmin(request):

    orders = Order.objects.all().filter(ordered=True, status='Pending')
    context = {
        "order": orders
    }
    return render(request, 'orders/order_preview.html', context)

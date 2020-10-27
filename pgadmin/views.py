from django.shortcuts import render, redirect
from menus.models import Menu, Category
from accounts.models import Customer
from cart.models import Order
from checkout.models import BillingAddress
from .forms import *
# Create your views here.


def adminView(request):
    pending_orders = Order.objects.all().filter(ordered=True, status='Pending')
    customer = Customer.objects.all()
    context = {
        "pending_orders": pending_orders,
        'customer': customer
    }
    return render(request, 'dashboard.html', context)


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
    pending_orders = Order.objects.all().filter(ordered=True, status='Pending')
    delivered_orders = Order.objects.all().filter(ordered=True, status='Delivered')
    out_orders = Order.objects.all().filter(ordered=True, status='Out for delivery')
    cancled_orders = Order.objects.all().filter(ordered=True, status='Canceled')
    context = {
        "pending_orders": pending_orders,
        "delivered_orders": delivered_orders,
        "out_orders": out_orders,
        "cancled_orders": cancled_orders,
    }

    return render(request, 'orders/order_preview.html', context)


def customerViewAdmin(request, id):
    customer = Customer.objects.all().filter(id=id)
    address = BillingAddress.objects.all().filter(customer_id=id)
    context = {
        'customer': customer,
        'address': address
    }
    return render(request, 'orders/customer_preview.html', context)


def orderForm(request, id=id):

    if request.method == "GET":
        if id == 0:
            form = OrderStatusForm()
        else:
            order = Order.objects.get(id=id)
            form = OrderStatusForm(instance=order)
        return render(request, "orders/order_form.html", {'form': form})
    else:
        if id == 0:
            form = OrderStatusForm(request.POST)
        else:
            order = Order.objects.get(id=id)
            form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('ordersadmin')

from django.shortcuts import render, redirect
from menus.models import Menu, Category
from accounts.models import Customer
from cart.models import Order
from checkout.models import BillingAddress
from .forms import *
from .filters import *
from django.contrib.auth.decorators import login_required
from accounts.decorators import *
# Create your views here.


@login_required
@allowed_users(allowed_roles=['Admin'])
def adminView(request):

    orders = Order.objects.all().filter(ordered=True)
    total_orders = orders.count()
    out_orders = Order.objects.all().filter(
        ordered=True, status='Out for delivery')
    for_delivery = out_orders.count()
    pending_orders = Order.objects.all().filter(
        ordered=True, status='Pending')
    pending = pending_orders.count()

    customer = Customer.objects.all()
    context = {
        'customer': customer,
        'total_orders': total_orders,
        "pending": pending,
        'for_delivery': for_delivery,
        "pending_orders": pending_orders,


    }
    return render(request, 'dashboard.html', context)


@allowed_users(allowed_roles=['Admin'])
def menuAdminView(request):
    menu = Menu.objects.all()
    mFilter = MenuFilter(request.GET, queryset=menu)
    menu = mFilter.qs
    context = {
        'menu': menu,
        'mFilter': mFilter
    }
    return render(request, 'menu/menu_admin.html', context)


@allowed_users(allowed_roles=['Admin'])
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


@allowed_users(allowed_roles=['Admin'])
def menu_delete(request, id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    return redirect('menuadmin')


@allowed_users(allowed_roles=['Admin'])
def categoryView(request):
    category = Category.objects.all()
    mFilter = CategoryFilter(request.GET, queryset=category)
    category = mFilter.qs
    context = {
        'category': category,
        'mFilter': mFilter
    }
    return render(request, 'category/category_admin.html', context)


@allowed_users(allowed_roles=['Admin'])
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


@allowed_users(allowed_roles=['Admin'])
def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('categoryadmin')


@allowed_users(allowed_roles=['Admin'])
def customerView(request):
    customer = Customer.objects.all()
    mFilter = CustomerFilter(request.GET, queryset=customer)
    customer = mFilter.qs
    context = {
        'customer': customer,
        'mFilter': mFilter
    }
    return render(request, 'accounts/customers.html', context)


@allowed_users(allowed_roles=['Admin'])
def orderViewAdmin(request):

    orders = Order.objects.all().filter(ordered=True)

    mFilter = OrderFilter(request.GET, queryset=orders)
    orders = mFilter.qs
    context = {
        'orders': orders,
        'mFilter': mFilter
    }

    return render(request, 'orders/order_preview.html', context)


@allowed_users(allowed_roles=['Admin'])
def customerViewAdmin(request, id):
    customer = Customer.objects.all().filter(id=id)
    address = BillingAddress.objects.all().filter(customer_id=id)
    context = {
        'customer': customer,
        'address': address
    }
    return render(request, 'orders/customer_preview.html', context)


@allowed_users(allowed_roles=['Admin'])
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

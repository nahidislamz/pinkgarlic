from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Cart, Order
from accounts.models import Customer
from menus.models import Menu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def cartView(request):

    customer = request.user.customer
    cart = Cart.objects.filter(customer=customer, purchased=False)
    orders = Order.objects.filter(customer=customer, ordered=False)

    if cart.exists():
        order = orders[0]
        return render(request, 'shopping_cart.html', {'cart': cart, 'order': order})

    else:
        return render(request, 'cart_empty.html')


@login_required
def add_to_cart(request, id):
    item = get_object_or_404(Menu, id=id)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        customer=request.user.customer,
        purchased=False
    )
    order_qs = Order.objects.filter(
        customer=request.user.customer, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, f"{item.title} quantity has updated.")

            return redirect("menu")
        else:
            order.orderitems.add(order_item)
            messages.info(request, f"{item.title}  was added to your cart")

            return redirect("menu")
    else:
        order = Order.objects.create(
            customer=request.user.customer)
        order.orderitems.add(order_item)
        messages.info(request, f"{item.title}  was added to your cart")
        return redirect("menu")


@login_required
def increaseItem(request, id):

    item = get_object_or_404(Menu, id=id)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        customer=request.user.customer,
        purchased=False
    )
    order_qs = Order.objects.filter(
        customer=request.user.customer, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f"{item.title} quantity has updated.")
            return redirect("cart")

        else:
            order.orderitems.add(order_item)
            return redirect("cart")
    else:
        order = Order.objects.create(
            customer=request.user.customer)
        order.orderitems.add(order_item)
        return redirect("cart")


@login_required
def decreaseItem(request, id):
    item = get_object_or_404(Menu, id=id)
    order_qs = Order.objects.filter(
        customer=request.user.customer,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item = Cart.objects.filter(
                item=item,
                customer=request.user.customer,
                purchased=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
            messages.info(request, f"{item.title} has been removed.")
            return redirect("cart")
        else:
            messages.info(request, f"{item.title} quantity has updated.")
            return redirect("cart")
    else:
        messages.error(request, "You do not have an active order")
        return redirect("cart")

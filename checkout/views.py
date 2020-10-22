from django.shortcuts import render, redirect
from .models import BillingAddress
from .form import BillingForm
from cart.models import Order, Cart
import stripe
from django.conf import settings
from django.utils.crypto import get_random_string


def checkout(request):

    form = BillingForm

    cart = Cart.objects.filter(customer=request.user.customer, purchased=False)

    order_qs = Order.objects.filter(
        customer=request.user.customer, ordered=False)

    order_items = order_qs[0].orderitems.all()

    order_total = order_qs[0].getOrder_total()

    context = {"form": form, "order_items": order_items,
               "order_total": order_total, 'cart': cart}

    # Getting the saved saved_address
    saved_address = BillingAddress.objects.filter(
        customer=request.user.customer)
    if saved_address.exists():
        savedAddress = saved_address.first()
        context = {"form": form, "order_items": order_items,
                   "order_total": order_total, "savedAddress": savedAddress, 'cart': cart}
    if request.method == "POST":
        saved_address = BillingAddress.objects.filter(
            customer=request.user.customer)
        if saved_address.exists():

            savedAddress = saved_address.first()
            form = BillingForm(request.POST, instance=savedAddress)
            if form.is_valid():
                billingaddress = form.save(commit=False)
                billingaddress.customer = request.user.customer
                billingaddress.save()
        else:
            form = BillingForm(request.POST)
            if form.is_valid():
                billingaddress = form.save(commit=False)
                billingaddress.customer = request.user.customer
                billingaddress.save()
                return redirect('checkout')

    return render(request, 'checkout_address.html', context)


def payment(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    order_qs = Order.objects.filter(
        customer=request.user.customer, ordered=False)
    order_total = order_qs[0].getOrder_total()
    totalCents = float(order_total * 100)
    total = round(totalCents, 2)
    if request.method == 'POST':
        charge = stripe.Charge.create(amount=total,
                                      currency='usd',
                                      description=order_qs,
                                      source=request.POST['stripeToken'])

    return render(request, 'payment.html', {"key": key, "total": total})


def charge(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    order = Order.objects.get(customer=request.user.customer, ordered=False)
    order_total = order.getOrder_total()
    totalCents = int(float(order_total * 100))
    if request.method == 'POST':
        charge = stripe.Charge.create(amount=totalCents,
                                      currency='usd',
                                      description=order,
                                      source=request.POST['stripeToken'])
        if charge.status == "succeeded":
            orderId = get_random_string(
                length=16, allowed_chars=u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            print(charge.id)
            order.ordered = True
            order.paymentId = charge.id
            order.orderId = f'#{request.user.customer}{orderId}'
            order.save()
            cartItems = Cart.objects.filter(customer=request.user.customer)
            for item in cartItems:
                item.purchased = True
                item.save()
        return render(request, 'charge.html')


def oderView(request):

    try:
        orders = Order.objects.filter(
            customer=request.user.customer, ordered=True)
        context = {
            "orders": orders
        }
    except:
        messages.warning(request, "You do not have an active order")
        return redirect('menu')
    return render(request, 'ordered.html', context)

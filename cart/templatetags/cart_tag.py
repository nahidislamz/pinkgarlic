from django import template
from cart.models import Order, Cart

register = template.Library()


@register.filter
def cart_count(customer):
    order = Order.objects.filter(customer=customer, ordered=False)

    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0

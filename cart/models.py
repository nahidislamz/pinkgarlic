from djongo import models
from accounts.models import Customer
from menus.models import Menu


class Cart(models.Model):
    #id = models.ObjectField()
    item = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'
    # Getting the total price

    def getCart_total(self):
        total = self.item.price * self.quantity
        floattotal = float("{0:.2f}".format(total))
        return floattotal


class Order(models.Model):
    OPTION = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    )
    orderitems = models.ManyToManyField(Cart)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    status = models.CharField(
        max_length=200, null=True, choices=OPTION, default=OPTION[0][0])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order from {self.customer.first_name} {self.customer.last_name}  Phone: {self.customer.phone}'

    def getOrder_total(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.getCart_total()

        return total

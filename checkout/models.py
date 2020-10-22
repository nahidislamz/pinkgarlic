from djongo import models
from accounts.models import Customer


class BillingAddress(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'Address:  {self.address}  |  Phone: ' + self.phone

    class Meta:
        verbose_name_plural = "Delivery Addresses"

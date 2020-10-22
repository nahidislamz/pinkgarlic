from django.forms import ModelForm
from .models import BillingAddress


class BillingForm(ModelForm):

    class Meta:
        model = BillingAddress
        fields = ['address', 'zipcode', 'city', 'phone']

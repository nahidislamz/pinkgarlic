from django.forms import ModelForm
from django import forms
from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'profile_pic': '',
        }

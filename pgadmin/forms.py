from django import forms
from menus.models import Menu, Category
from cart.models import Order


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('title', 'description', 'category', 'price')
        labels = {
            'title': 'Item Name',
            'price': 'price £',
        }

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('category',)
        labels = {
            'category': 'Category Name',
        }


class OrderStatusForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('status',)

    def __init__(self, *args, **kwargs):
        super(OrderStatusForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "update status"

from django import forms
from menus.models import Menu, Category


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

import django_filters
from menus.models import Menu, Category
from cart.models import Order
from accounts.models import Customer


class MenuFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains', label='Search By Name')

    class Meta:
        model = Menu
        fields = ['category', ]


class CategoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category', lookup_expr='icontains', label='Search Category')

    class Meta:
        model = Category
        fields = ['category', ]


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = ['status', ]


class CustomerFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(
        field_name='email', lookup_expr='icontains', label='Search By Email')

    class Meta:
        model = Customer
        fields = ['email', 'phone', ]

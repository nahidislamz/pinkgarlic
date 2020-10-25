from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', adminView, name='pgadmin'),
    # accounts section
    path('customers/', customerView, name='customer'),
    # menu section
    path('menuadmin/', menuAdminView, name='menuadmin'),
    path('addmenu/', menu_form, name='addmenu'),
    path('addmenu/<id>', menu_form, name='menu_update'),
    path('mdelete/<int:id>', menu_delete, name='menu_delete'),

    # category section
    path('categoryadmin/', categoryView, name='categoryadmin'),
    path('addcategory/', category_form, name='addcategory'),
    path('addcategory/<int:id>', category_form, name='category_update'),
    path('cdelete/<int:id>', category_delete, name='category_delete'),

    # Order Section
    path('orders/', orderViewAdmin, name='ordersadmin'),
    path('orders/<int:id>', orderForm, name='order_update'),

]

from django.contrib import admin
from .models import Category, Menu
# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'price')
    list_filter = ('title', 'category')
    #search_fields =('title','category')


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category)

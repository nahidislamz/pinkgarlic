from django.contrib import admin

# Register your models here.
from .models import Customer


class CoustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user', 'phone', 'profile_pic')


admin.site.register(Customer, CoustomerAdmin)

from djongo import models

# Create your models here.
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.category


class Menu(models.Model):

    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1000, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    price = models.FloatField('£', null=True)

    def __str__(self):
        return self.title

from django.contrib import admin
from . models import Categories, Products, Order, OrderItem

#Register your models here.
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Order)
admin.site.register(OrderItem)
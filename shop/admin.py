from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','discount_price')
    list_display_links= ('id', 'title')
    search_fields = ['title','description']

class CartAdmin(admin.ModelAdmin):
    list_display = ('product','user', 'quantity')
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
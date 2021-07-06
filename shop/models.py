from django.db import models
from django.contrib.auth.models import User
import math

from django.db.models.aggregates import Max
from django.urls.base import set_urlconf


class Product(models.Model):
    color_choice = (
        ('G', 'Green'),
        ('B', 'Blue'),
        ('Gr', 'Gray'),
        ('Y', 'Yellow'),
        ('R','Red'),
    )
    categories_choice = (
        ('BS', 'BLUCHER SHOE'),
        ('CS', 'CLOG SHOE'),
        ('SBS', 'SNOW BOOT SHOE'),
        ('GS', 'GALESH SHOE'),
        ('PS', 'PATAUGAS SHOE'),
        ('JS', 'JAZZ SHOE'),

    )
    sizes_choice = (
        ('5.5','5.5'),
        ('6','6'),
        ('6.5','6.5'),
        ('7','7'),
        ('7.5','7.5'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    overview = models.TextField(max_length=500)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True, default=0)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(blank= True)
    image_1 = models.ImageField(blank= True, default = '')
    image_2 = models.ImageField(blank= True, default = '')
    image_3 = models.ImageField(blank= True, default = '')
    colors = models.CharField(choices=color_choice, max_length=2, default='Green')
    categories = models.CharField(choices=categories_choice, max_length=3, default='BLUCHER SHOE')
    sizes = models.CharField(choices=sizes_choice, max_length=3, default='5.5')

    @property
    def image_url(self):
        url = ''
        if self.image:
            url = self.image
            return url

    @property
    def image_url_1(self):
        url = ''
        if self.image_1:
            url = self.image_1
            return url

    @property
    def image_url_2(self):
        url = ''
        if self.image_2:
            url = self.image_2
            return url

    @property
    def image_url_3(self):
        url = ''
        if self.image_3:
            url = self.image_3
            return url

    def __str__(self) -> str:
        return self.title



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.title
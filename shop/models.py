from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    image = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
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
    image_1 = models.ImageField(blank= True, default = '', null= True)
    image_2 = models.ImageField(blank= True, default = '', null= True)
    image_3 = models.ImageField(blank= True, default = '', null= True)
    colors = models.ForeignKey(Color, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.CharField(choices=sizes_choice, max_length=3, default='5.5')

    @property
    def image_url(self):
        url = ''
        if self.image:
            url = self.image
        return url

    def __str__(self) -> str:
        return self.title



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.title


class userAddress(models.Model):
    select_address = (
        
        ('--', '------'),
        ('of', 'Office'),
        ('ho', 'Home'),
        ('co', 'Commercial'),
    )
    full_name = models.CharField(max_length=10)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=6)
    town = models.CharField(max_length=100)
    address = models.CharField(choices=select_address, max_length=2)
        
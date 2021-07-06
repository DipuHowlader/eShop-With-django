from typing import ValuesView
from django.urls import path 
from .views import *

app_name = 'shop'
urlpatterns =[
    path('', home, name='homePage'),
    path('search/', search, name='searchPage'),
    path('cart/', cart.as_view(), name='cartPage'),
    path('checkout/', checkout.as_view(), name='checkoutPage'),
    path('products/', products.as_view(), name='productsPage'),
    path('<int:pk>/single/', singleProduct.as_view(), name='singleProductPage'),
    path('update_data/', updateData, name='updateData'),
]

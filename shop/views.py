from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.db.models.expressions import F
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, resolve_url
from django.urls.base import reverse_lazy
from django.views import View
from django.contrib import messages
from .forms import customUserCreationForm, customerAddress
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from .models import Product, Cart
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
import json

def cartInformation(request):
    total = 0 
    cartQuantity = 0
    if request.user.is_authenticated:
        cartQuantity = len([item for item in Cart.objects.filter(user = request.user)])
        total = sum([item.price for item in Cart.objects.filter(user = request.user)])
    return ({'total': total,
        'quantity' : cartQuantity})

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html',{'products': products,'cartData' :cartInformation(request)})


def search(request):
    if request.method == "GET":
        keyword = request.GET['keyword']   
        if keyword:  
            products = [item for item in Product.objects.filter(title__icontains=keyword)]
            products += Product.objects.filter(description__icontains=keyword)
            return render(request, 'shop/search.html', {'products':products,'cartData' :cartInformation(request)})

class cart(View):
    def get(self, request):
        cart = []
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
        return render(request,'shop/cart.html', {'carts':cart,'cartData' :cartInformation(request)})


class checkout(View):
    def get(self, request):
        form = customerAddress
        return render(request, 'shop/checkout.html', {'cartData' :cartInformation(request),
                                                        'forms':form
                                                        })
    

class products(View):
    def get(self, request):
        paginator = Paginator(Product.objects.all(), 9)
        page = paginator.page(request.GET.get('page', 1))
        return render(request,'shop/products.html',{'cartData' :cartInformation(request),
                                                 'products' : page})

class singleProduct(View):
    def get(self, request, pk):
        
        paginator = Paginator(Product.objects.all(), 6)
        page = paginator.page(request.GET.get('page', 1))
        product = Product.objects.get(id = pk)
        return render(request, 'shop/single.html', {'theProduct': product,
                                                    'products': page,
                                                    'cartData' :cartInformation(request),
                                                    'demo': Product
                                                    })


class accounts(View):
    def get(self, request, *args, **kwargs):
        form = customUserCreationForm
        login_form = AuthenticationForm()
        return render(request, 'shop/account.html', {'form': form,
                                                    'login_form' :login_form,
                                                   'cartData' :cartInformation(request)})

    def post(self, request, *args, **kwargs):
        login_form = AuthenticationForm()
        form = customUserCreationForm(request.POST)
        if request.POST.get('submit') == 'sign up':
            if form.is_valid():
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                username =  first_name + ' ' + last_name
                email = request.POST['email']
                password = request.POST['password1']
                if User.objects.filter(username = username):
                    messages.error(request,'someone with this name is already exists!!')
                else:
                    User.objects.create_user(username, email, password, 
                                            first_name = first_name, 
                                            last_name = last_name,)
                    user = authenticate(request,username = username, password = password)
                    login(request, user)
                    messages.success(request, 'Congratulations!! Registered successfully')
                    return redirect ('/')
        else:
            form = customUserCreationForm()
        
        if request.POST.get('submit') == 'Login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            # login_form = AuthenticationForm(request.POST)
            user = authenticate(request,username = username, password = password)
            if user is not None:
                messages.success(request, 'you have logged in Successfully!!')
                login(request,user)
                return redirect ('/')
            else:
                messages.error(request, 'Email and passsword combination doesn\'t match')
        print(form, login_form)
        return render(request, 'shop/account.html', {'form': form, 'login_form' :login_form,
                                                   'cartData' :cartInformation(request)
                                                    })

def updateData(request):
    data = json.loads(request.body)
    action = data['action']
    productID = data['product']
    product = Product.objects.get(id = productID)
    if action == 'add':
        cart = [item.product.id for item in Cart.objects.filter(user = request.user)]
        if product and product.id not in cart:
            Cart.objects.create(user = request.user, product=product)
            messages.success(request, 'Product is added to cart !!')

        if product.id in cart:
            increase = Cart.objects.filter(product = product).get(user=request.user)
            increase.quantity += 1
            increase.save()

    elif action == 'increase':
        cart = Cart.objects.filter(product = product)
        cart = cart.get(user = request.user)
        cart.quantity +=1
        cart.save()

    elif action == 'decrease':
        cart = Cart.objects.filter(product = product)
        cart = cart.get(user = request.user)
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()

    elif action == 'remove':
        Cart.objects.filter(product = product).get(user=request.user).delete()

    return (JsonResponse({
        'item': 'updated'
    },safe= False))


class changePasswordView(LoginRequiredMixin,View):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'accounts/passwordChange.html', {'form': form, 'cartData' :cartInformation(request)})

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully !!')
            logout(request)
            return redirect(reverse_lazy('accountPage'))
        else:
            messages.error(request, 'please correct the error below')
        return render(request, 'accounts/passwordChange.html', {'form':form, 'cartData' :cartInformation(request)})


class paymentPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shop/payment.html')
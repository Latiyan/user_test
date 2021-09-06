from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, Orders

# def home(request):
#     return render(request, 'app/home.html')

class HomeView(View):
    def get(self, request):
        constants = {
            'topwears': Product.objects.filter(category='TW'),
            'bottomwears': Product.objects.filter(category='BW'),
            'mobiles': Product.objects.filter(category='M'),
            'laptops': Product.objects.filter(category='L'),
        }

        return render(request, 'app/home.html', constants)

class PeoductDetailView(View):
    def get(self,request, pk):
        constants = {
            'product': Product.objects.get(pk=pk)
        }

        return render(request, 'app/productdetail.html', constants)

def add_to_cart(request):
    return render(request, 'app/addtocart.html')

def buy_now(request):
    return render(request, 'app/buynow.html')

def profile(request):
    return render(request, 'app/profile.html')

def address(request):
    return render(request, 'app/address.html')

def orders(request):
    return render(request, 'app/orders.html')

def change_password(request):
    return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(sale_price__gt=1000) # Here __gt means greater than
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(sale_price__lt=1000) # Here __lt means less than
    else:
        mobiles = Product.objects.filter(category='M').filter(brand=data)

    constants = {
        'mobiles': mobiles,
    }

    return render(request, 'app/mobile.html', constants)

def login(request):
    return render(request, 'app/login.html')

def customerregistration(request):
    return render(request, 'app/customerregistration.html')

def checkout(request):
    return render(request, 'app/checkout.html')

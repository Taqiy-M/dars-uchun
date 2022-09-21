from django.shortcuts import render

# Create your views here.
from django.views import View
from userapp.models import Account
from .models import *


class CartView(View):
    def get(self, request):
        account = Account.objects.get(user=request.user)
        cart = Cart.objects.get(account=account, history=False)


        if cart == None:
            cart = Cart.objects.create(account=account)

        orders = cart.order.all()
        s = 0
        d = 0


        for i in orders:
            a = i.quantity*i.product.price
            d += i.discount
            s += a
            i.cost = a
        t = s - d
        cart.cost = t
        print(orders.count())
        data = {
            'orderlar': orders,
            'summa': s,
            'discount': d,
            'final_price': t
        }
        return render(request, 'page-shopping-cart.html', data)



class ProfileOrders(View):
    def get(self, request):

        user = Account.objects.get(user=request.user)
        carts = Cart.objects.filter(history=True, account=user)
        data = {
            'savatlar': carts
        }
        return render(request, 'page-profile-orders.html', data)

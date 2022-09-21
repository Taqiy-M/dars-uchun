from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .models import *
from userapp.models import Account
from sotuvapp.models import *

class HomeView(View):
    def get(self, request):
        data = {
            'categories': Category.objects.all()[:5]
        }
        return render(request, 'page-index-2.html', data)


class Home2View(View):
    def get(self, request):
        data = {
            'categories': Category.objects.all()
        }
        return render(request, 'page-index.html', data)

class AllCategories(View):
    def get(self, request):
        return render(request, 'page-category.html')

class AllProducts(View):
    def get(self, request):
        data = {
            'mahsulotlar': Product.objects.all(),
            'count': Product.objects.all().count()
        }
        return render(request, 'page-listing-grid.html', data)


class SingleProduct(View):
    def get(self, request, a):
        pr = Product.objects.get(id=a)
        comment = Comment.objects.filter(product=pr)
        data = {
            'mahsulot': pr,
            'comments': comment
        }
        return render(request, 'page-detail-product.html', data)

    def post(self, request, a):
        comment_text = request.POST.get('comment')
        user = request.user
        account = Account.objects.get(user=user)
        product = Product.objects.get(id=a)
        Comment.objects.create(comment=comment_text, user=account, product=product)
        return redirect(f"/product/{a}/")


class OrderSingleProduct(View):
    def get(self, request, a):
        user = request.user
        account = Account.objects.get(user=user)
        product = Product.objects.get(id=a)
        order = Order.objects.create(product=product)
        cart = Cart.objects.filter(account=account, history=False)
        if len(cart) == 0:
            cart = Cart.objects.create(account=account)
            cart.order.add(order)
            return redirect("/cart/")
        cart[0].order.add(order)
        return redirect('/cart/')













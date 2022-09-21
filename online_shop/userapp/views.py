from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .models import Account


class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
            lo = request.POST.get('username')
            pa = request.POST.get('password')
            user = authenticate(username=lo, password=pa)
            if user is None:
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/home/')


class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        name = request.POST.get('name')
        passw = request.POST.get('pass_create')
        passw_repeat = request.POST.get('pass_repeat')
        if passw == passw_repeat:
            user = User.objects.create_user(username=name, password=passw)
            Account.objects.create(user=user, ism=name)
            login(request, user)
            return redirect('/home/')
        else:
            return redirect('/register/')



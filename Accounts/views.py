from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.contrib import auth, messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from Accounts.forms import LoginForm


# Create your views here.

@method_decorator(login_required, name='dispatch')
class Home(View):
    template_name = 'Accounts/home.html'

    def get(self, request):
        context = {
            'msg': 'Hello'
        }
        return render(request, self.template_name, context)
    
class Login(View):
    template_name = 'Accounts/login.html'

    def post(self, request):
        form =  LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = auth.authenticate(email=email, password=password)
            if user: 
                auth.login(request, user)
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')


        context = {
            'msg': 'Hello'
        }
        return redirect('Accounts:home')
    
    def get(self, request):
        if request.user.is_authenticated: return redirect("Accounts:home")

        context = {
            'form': LoginForm(),  
            'msg': 'Hello'
        }
        return render(request, self.template_name, context)
    
class Logout(View):
    def get(self, request):
        auth.logout(request)
        messages.success(request,'Logged Out Successfully!')
        return redirect('Accounts:login') 

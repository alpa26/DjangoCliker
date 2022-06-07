# Create your views here.
from django.shortcuts import render,redirect  
from django.http import HttpResponse 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from rest_framework.views import APIView

def index(request):
    return HttpResponse('index page')

def test(request):
    return HttpResponse('test page')

class Register(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = UserForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            return redirect('index')
        return render(request, 'register.html', {'form': form})


class User_login(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request):
        form = UserForm()
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password')) 
        if user:
            login(request, user) 
            return redirect('index')
        return render(request, 'login.html', {'form': form, 'invalid': True})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
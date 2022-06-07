# Create your views here.
from django.shortcuts import render,redirect  
from django.http import HttpResponse 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from rest_framework.views import APIView
from .serializers import CoreSerializer, BoostSerializer
from rest_framework.decorators import api_view
from .models import Core,Boost
from rest_framework.response import Response
from rest_framework import viewsets

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

            core = Core(user=user) 
            core.save() 
            return redirect('index')

        return render(request, 'register.html', {'form': form})


class Login(APIView):
    form = UserForm()
    def get(self, request):
        return render(request, 'login.html', {'form': self.form})

    def post(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password')) 
        if user:
            login(request, user) 
            return redirect('index')
        return render(request, 'login.html', {'form': self.form, 'invalid': True})




@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    core = Core.objects.get(user=request.user)
    boosts = Boost.objects.filter(core=core) # Достаем бусты пользователя из базы
   
    return render(request, 'index.html', {
        'core': core,
        'boosts': boosts, # Возвращаем бусты на фронтик
    })

@api_view(['GET'])
@login_required
def call_click(request):
    core = Core.objects.get(user=request.user)
    is_levelup = core.click() # Труе если буст создался
    if is_levelup:
        Boost.objects.create(core=core, price=core.level*50, power=core.level*20) # Создание буста 
    core.save()

    return Response({ 'core': CoreSerializer(core).data, 'is_levelup': is_levelup })


class BoostViewSet(viewsets.ModelViewSet): 
    queryset = Boost.objects.all() 
    serializer_class = BoostSerializer

    # Переопределение метода get_queryset для получения бустов, привязанных к определенному ядру
    def get_queryset(self):
        core = Core.objects.get(user=self.request.user) # Получение ядра пользователя
        boosts = Boost.objects.filter(core=core) # Получение бустов ядра
        return boosts
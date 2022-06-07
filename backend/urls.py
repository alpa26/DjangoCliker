from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.User_login.as_view(), name='login'),
    path('', views.User_login.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
]
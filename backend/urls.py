from django.urls import path
from . import views

boosts = views.BoostViewSet.as_view({ 
    'get': 'list', 
    'post': 'create', 
})

lonely_boost = views.BoostViewSet.as_view({
    'put': 'partial_update', 
})

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('call_click/', views.call_click),
    path('', views.index, name='index'),
    path('boost/<int:pk>/', lonely_boost, name='boost'),
    path('boosts/', boosts, name='boosts')
]
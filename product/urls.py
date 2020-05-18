from django.urls import path
from product import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('burger/', views.burger, name='burger'),
    path('chinese/', views.chinese, name='chinese'),
    path('beverages/', views.beverages, name='beverages'),
    path('sandwich/', views.sandwich, name='sandwich'),
    path('pizza/', views.pizza, name='pizza'),
    path('snacks/', views.snacks, name='snacks'),
    
]
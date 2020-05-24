from django.urls import path
from product import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('burger/', views.burger, name='burger'),
    path('<int:pk>/<str:slug>/burger/', views.BurgerDetailView.as_view(), name="burger_detail"),
    path('chinese/', views.chinese, name='chinese'),
    path('<int:pk>/<str:slug>/chinese/', views.ChineseDetailView.as_view(), name="chinese_detail"),
    path('beverages/', views.beverages, name='beverages'),
    path('<int:pk>/<str:slug>/beverages/',views.BeveragesDetailView.as_view(), name="beverages_detail"),
    path('sandwich/', views.sandwich, name='sandwich'),
    path('<int:pk>/<str:slug>/sandwich/',views.SandwichDetailView.as_view(), name="sandwich_detail"),
    path('pizza/', views.pizza, name='pizza'),
    path('<int:pk>/<str:slug>/pizza/',views.PizzaDetailView.as_view(), name="pizza_detail"),
    path('snacks/', views.snacks, name='snacks'),
    path('<int:pk>/<str:slug>/snacks/',views.SnacksDetailView.as_view(), name="snacks_detail"),
    path('cart/', views.cart, name='cart'),
    path('tracker/', views.tracker, name='tracker'),
    path('checkout/', views.checkout, name='checkout'),
    
]
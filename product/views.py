from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from product.models import Burger, Beverages, Chinese, Pizza, Sandwich, Snacks, Home
from django.views import View


# Create your views here.
def home(request):
    data8 = Home.objects.all()
    return render(request, 'index.html', {'data8': data8})

def about(request):
    return render(request, 'pages/about.html')


def menu(request):
    return render(request, 'pages/menu.html')

@login_required(login_url='/login/')
def burger(request):
    data1 = Burger.objects.all()
    return render(request, 'pages/burger.html', {'data1': data1 })

@login_required(login_url='/login/')
def chinese(request):
    data2 = Chinese.objects.all()
    return render(request, 'pages/chinese.html', {'data2': data2 })

def beverages(request):
    data3 = Beverages.objects.all()
    return render(request, 'pages/beverages.html', {'data3': data3 })

@login_required(login_url='/login/')
def sandwich(request):
    data4 = Sandwich.objects.all()
    return render(request, 'pages/sandwich.html', {'data4': data4 })

@login_required(login_url='/login/')
def pizza(request):
    data5 = Pizza.objects.all()
    return render(request, 'pages/pizza.html', {'data5': data5 })

@login_required(login_url='/login/')
def snacks(request):
    data6 = Snacks.objects.all()
    return render(request, 'pages/snacks.html', {'data6': data6 })




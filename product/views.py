from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from product.models import Burger, Chinese, Beverages, Sandwich, Pizza, Snacks, Home
from django.views import View
from product.models import *



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

class BurgerDetailView(DetailView):
    model = Burger
    template_name = "product/burger_detail.html"
    context_object_name = "burger"
    #success_url = reverse_lazy("burger_detail")

    def get_context_data(self, **kwargs):
        context = super(BurgerDetailView,self).get_context_data(**kwargs)
        return context


@login_required(login_url='/login/')
def chinese(request):
    data2 = Chinese.objects.all()
    return render(request, 'pages/chinese.html', {'data2': data2 })

class ChineseDetailView(DetailView):
    model = Chinese
    template_name = "product/chinese_detail.html"
    context_object_name = "chinese"
    #success_url = reverse_lazy("chinese_detail")

    def get_context_data(self, **kwargs):
        context = super(ChineseDetailView,self).get_context_data(**kwargs)
        return context

def beverages(request):
    data3 = Beverages.objects.all()
    return render(request, 'pages/beverages.html', {'data3': data3 })

class BeveragesDetailView(DetailView):
    model = Beverages
    template_name = "product/beverages_detail.html"
    context_object_name = "beverages"
    #success_url = reverse_lazy("beverages_detail")

    def get_context_data(self, **kwargs):
        context = super(BeveragesDetailView,self).get_context_data(**kwargs)
        return context


@login_required(login_url='/login/')
def sandwich(request):
    data4 = Sandwich.objects.all()
    return render(request, 'pages/sandwich.html', {'data4': data4 })

class SandwichDetailView(DetailView):
    model = Sandwich
    template_name = "product/sandwich_detail.html"
    context_object_name = "sandwich"
    #success_url = reverse_lazy("peverages_detail")

    def get_context_data(self, **kwargs):
        context = super(SandwichDetailView,self).get_context_data(**kwargs)
        return context


@login_required(login_url='/login/')
def pizza(request):
    data5 = Pizza.objects.all()
    return render(request, 'pages/pizza.html', {'data5': data5 })

class PizzaDetailView(DetailView):
    model = Pizza
    template_name = "product/pizza_detail.html"
    context_object_name = "pizza"
    #success_url = reverse_lazy("peverages_detail")

    def get_context_data(self, **kwargs):
        context = super(PizzaDetailView,self).get_context_data(**kwargs)
        return context



@login_required(login_url='/login/')
def snacks(request):
    data6 = Snacks.objects.all()
    return render(request, 'pages/snacks.html', {'data6': data6 })

class SnacksDetailView(DetailView):
    model = Snacks
    template_name = "product/snacks_detail.html"
    context_object_name = "snacks"
    #success_url = reverse_lazy("snacks_detail")

    def get_context_data(self, **kwargs):
        context = super(SnacksDetailView,self).get_context_data(**kwargs)
        return context

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = order.objects.get_or_created(customer=customer, compile=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items': items}
    return render(request, 'pages/cart.html')

def tracker(request):
    return render(request, 'pages/tracker.html')

def checkout(request):
    return render(request, 'pages/checkout.html')




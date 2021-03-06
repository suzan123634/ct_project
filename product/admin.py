from django.contrib import admin
from .models import Burger, Beverages, Chinese, Pizza, Sandwich, Snacks, Home, Order, OrderItem, ShippingAddress

# Register your models here.
class BugerAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'price']
    list_display = [ 'title', 'price', 'slug', 'reporter', 'image']
    list_editable = ['price']
    list_filter = ['title','price']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Burger

class BeveragesAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'price']
    list_display = [ 'title', 'price', 'slug', 'reporter', 'image']
    list_editable = ['price']
    list_filter = ['title','price']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Beverages

class ChineseAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'price']
    list_display = [ 'title', 'price', 'slug', 'reporter', 'image']
    list_editable = ['price']
    list_filter = ['title','price']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Chinese

class PizzaAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'price']
    list_display = [ 'title', 'price', 'slug', 'reporter', 'image']
    list_editable = ['price']
    list_filter = ['title','price']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Pizza

class SandwichAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'price']
    list_display = [ 'title', 'price', 'slug', 'reporter', 'image']
    list_editable = ['price']
    list_filter = ['title','price']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Sandwich

class SnacksAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'price']
    list_display = [ 'title', 'price', 'slug', 'reporter', 'image']
    list_editable = ['price']
    list_filter = ['title','price']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Snacks

class HomeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [ 'name', 'images']
    list_filter = ['name']
    class Meta:
        model = Home

class OrderAdmin(admin.ModelAdmin):
    search_fields = ['customer', 'transaction_id']
    list_display = [ 'customer', 'transaction_id', 'date_order', 'complete']
    list_filter = ['customer','transaction_id']
    class Meta:
        model = Snacks

class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ['customer', 'Phone_number']
    list_display = [ 'customer', 'Phone_number', 'Hosteler', 'date_added']
    list_filter = ['customer','Phone_number']
    class Meta:
        model = Snacks



admin.site.register(Burger, BugerAdmin)
admin.site.register(Beverages, BeveragesAdmin)
admin.site.register(Chinese, ChineseAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Sandwich, SandwichAdmin)
admin.site.register(Snacks, SnacksAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress, ShippingAddressAdmin)

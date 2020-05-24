from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Burger(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    image = models.ImageField(upload_to='uploads')
    slug = models.SlugField(unique=True)
    reporter = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("burger_detail", kwargs={"pk": self.pk, "slug": self.slug})

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price


class Beverages(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    image = models.ImageField(upload_to='uploads')
    slug = models.SlugField(unique=True)
    reporter = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("beverages_detail", kwargs={"pk": self.pk, "slug": self.slug})

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price


class Chinese(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    image = models.ImageField(upload_to='uploads')
    slug = models.SlugField(unique=True)
    reporter = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("chinese_detail", kwargs={"pk": self.pk, "slug": self.slug})

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price


class Pizza(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    image = models.ImageField(upload_to='uploads')
    slug = models.SlugField(unique=True)
    reporter = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("pizza_detail", kwargs={"pk": self.pk, "slug": self.slug})

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price


class Sandwich(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    image = models.ImageField(upload_to='uploads')
    slug = models.SlugField(unique=True)
    reporter = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("sandwich_detail", kwargs={"pk": self.pk, "slug": self.slug})

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price


class Snacks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    image = models.ImageField(upload_to='uploads')
    slug = models.SlugField(unique=True)
    reporter = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("snacks_detail", kwargs={"pk": self.pk, "slug": self.slug})

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price


class Home(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product1 = models.ForeignKey(Burger, on_delete = models.SET_NULL, blank=True, null=True)
    product2 = models.ForeignKey(Pizza, on_delete = models.SET_NULL, blank=True, null=True)
    product3 = models.ForeignKey(Chinese, on_delete = models.SET_NULL, blank=True, null=True)
    product4 = models.ForeignKey(Beverages, on_delete = models.SET_NULL, blank=True, null=True)
    product5 = models.ForeignKey(Sandwich, on_delete = models.SET_NULL, blank=True, null=True)
    product6 = models.ForeignKey(Snacks, on_delete = models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    Phone_number = models.IntegerField()
    Hosteler = models.BooleanField(default=False, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    
        

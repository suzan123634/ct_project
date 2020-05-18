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


    def __str__(self):
        return self.title


    def get_price(self):
        return self.price


class Home(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.name

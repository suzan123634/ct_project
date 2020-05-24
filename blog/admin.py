from django.contrib import admin
from .models import Blog, Comment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title', 'reporter']
    list_display = [ 'title', 'image']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title', 'category', 'reporter']
    list_display = [ 'title', 'category', 'image']
    list_filter = ['title','category','reporter']
    class Meta:
        model = Blog

admin.site.register(Blog, BlogAdmin)

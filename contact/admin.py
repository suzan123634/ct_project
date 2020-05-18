from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'phone']
    list_display = [ 'name', 'email']
    list_filter = ['name','phone','email']
    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)
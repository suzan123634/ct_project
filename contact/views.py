from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.views import View

# Create your views here.
def contact(request):
    if request.method == "POST":
        message = request.POST.get('message', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        print(message, name, email, phone, subject)
        contact = Contact(message=message, name=name, email=email, phone=phone, subject=subject)
        contact.save()
    return render(request, 'pages/contact.html')


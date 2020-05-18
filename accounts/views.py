from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from accounts.forms import UserSignupForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
class UserSignUpView(View):
    template_name = "accounts/signup.html"

    def get(self, request):
        form = UserSignupForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password1']
            user.set_password(raw_password)
            user.save()
            
            return render(request, "accounts/signup_sucess.html")
        return render(request, self.template_name, {"form":form})



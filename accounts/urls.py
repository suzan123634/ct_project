from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views
from . import views
urlpatterns = [
    path('login/',LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/',LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),
    path('signup/',views.UserSignUpView.as_view(), name='signup'),
]

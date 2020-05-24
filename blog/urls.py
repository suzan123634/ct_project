from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('<int:pk>/<str:slug>/', views.BlogDetailView.as_view(), name="blog_detail"),
]
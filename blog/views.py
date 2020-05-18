from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from django.views import View

# Create your views here.


def blog(request):
    data7 = Blog.objects.all()
    return render(request, 'pages/blog.html', {'data7': data7})


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"
    # success_url = reverse_lazy("blog_detail")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count +1
        self.object.save()
        return context



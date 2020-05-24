from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    story = models.TextField()
    image = models.ImageField(upload_to='uploads')
    reporter = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    slug = models.SlugField(max_length=270)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk, "slug": self.slug})


    def __str__(self):
        return self.title

class Comment(models.Model):
    Post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')



    def __str__(self):
        return 'Comment by {}'.format(self.Name)




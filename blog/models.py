from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    CATEGORY = (("0", "Canteen_food"), ("1", "Product"), ("2", "Health"), ("3", "Inspiration"), ("4", "College_news"))
    title = models.CharField(max_length=150)
    story = models.TextField()
    image = models.ImageField(upload_to='uploads')
    reporter = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    category = models.CharField(choices=CATEGORY, max_length=2)
    slug = models.SlugField(max_length=270)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"category": self.get_category_display(),  "pk": self.pk, "slug": self.slug})


    def __str__(self):
        return self.title


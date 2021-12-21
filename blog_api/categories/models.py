from django.db import models
from posts.models import Post

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Category-Post Relationship"
        verbose_name_plural = "Categories-Posts Relationship"

    def __str__(self):
        post = Post.objects.get(pk=self.post.id)
        res = str(self.post) + " - " + str(self.category)
        return res
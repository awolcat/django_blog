from django.db import models
import uuid
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model
    """
    title = models.CharField(max_length=200)
    quote = models.TextField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')


class Comments(models.Model):
    """Comments model
    """
    content = models.TextField(max_length=300)
    article_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


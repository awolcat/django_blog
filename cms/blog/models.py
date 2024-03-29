from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    """Base model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel, models.Model):
    """Post model
    """
    title = models.CharField(max_length=200)
    quote = models.TextField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title


class Comments(BaseModel, models.Model):
    """Comments model
    """
    content = models.TextField(max_length=300)
    article_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.article_post.title


class Profile(BaseModel, models.Model):
    """Profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpeg')

    def __str__(self):
        return self.user.username
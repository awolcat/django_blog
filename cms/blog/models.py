from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BaseModel(models.Model):
    """Handles the creation of id, created_at and updated_at attributes for all classes"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class User(BaseModel, AbstractUser):
    """User model
    """
    USER_TYPES = (
                  ('A', 'Author'),
                  ('R', 'Reader')
                 )
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    user_type = models.CharField(choices=USER_TYPES)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=128)
    bio = models.CharField(max_length=250, blank=True)

class Article(BaseModel):
    """Article model
    """
    title = models.CharField(max_length=200)
    quote = models.TextField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)




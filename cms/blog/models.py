from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from tinymce import models as tinymce_models

class CategoriesEnum(models.TextChoices):
    LIFESTYLE = 'LS', _('Lifestyle')
    WORLD = 'W', _('World')
    BUSINESS = 'BS', _('Business')
    TECH = 'TC', _('Tech')
    DESIGN = 'DS', _('Design')
    CULTURE = 'CL', _('Culture')
    POLITICS = 'PL', _('Politics')
    OPINION = 'OP', _('Opinion')
    SCIENCE = 'SC', _('Science')
    HEALTH = 'HL', _('Health')
    STYLE = 'ST', _('Style')
    TRAVEL = 'TV', _('Travel')
    SPORTS = 'SP', _('Sports')  
    UNCATEGORIZED = 'UC',

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
    CategoriesEnum = CategoriesEnum
    title = models.CharField(max_length=200, null=True, blank=True)
    quote = models.TextField(max_length=300, null=True, blank=True )
    content = tinymce_models.HTMLField()
    image = models.ImageField(upload_to='images/', default='images/how-to-write-a-blog-post.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.CharField(max_length=2, choices=CategoriesEnum.choices, default=CategoriesEnum.UNCATEGORIZED)
    views = models.PositiveIntegerField(default=0)

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
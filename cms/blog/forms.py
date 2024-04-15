from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comments
#from .models import User

# Register the form for author signup
class UserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

# Register the form for author login
class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

# Register the form for creating a post
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'quote', 'content', 'image', 'author', 'category']

# Register the form for creating a comment
class CommentsForm(forms.ModelForm):
  class Meta:
    model = Comments
    fields = ['article_post', 'content']
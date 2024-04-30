from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comments
from django.db import models
from tinymce.widgets import TinyMCE


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
class PostForm(forms.Form):
    content = forms.CharField(widget=TinyMCE)
    title = forms.CharField()
    quote = forms.CharField()
    image = forms.ImageField()
    category = forms.ChoiceField(choices=Post.CategoriesEnum.choices) 

# Register the form for creating a comment
class CommentsForm(forms.ModelForm):
  class Meta:
    model = Comments
    fields = ['article_post', 'content']
  
  def __init__(self, *args, **kwargs):
    article_post = kwargs.pop('article_post')
    article_post = Post.objects.get(pk=article_post)
    super(CommentsForm, self).__init__(*args, **kwargs)
    self.fields['article_post'].widget = forms.HiddenInput()
    self.fields['article_post'].required = True
    self.fields['article_post'].label = ''
    self.fields['content'].widget.attrs['placeholder'] = 'Write a comment...'
    self.fields['content'].label = ''
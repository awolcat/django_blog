from django import forms
from .models import User

# Register the form for author signup
class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['firstname', 'lastname', 'email', 'password']

# Register the form for author login
class LoginForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['email', 'password']
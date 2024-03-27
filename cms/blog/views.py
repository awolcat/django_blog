from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def index(request):
    """Index page
    """
    return render(request, 'base.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')  # Assuming you have a URL named 'login'
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('') 
        else:
            messages.error(request, 'Invalid email or password.')
        return render(request, 'login.html')
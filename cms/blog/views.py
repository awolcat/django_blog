from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from .forms import UserForm, LoginForm, PostForm
from .models import Post


# Create your views here.

def index(request):
    """Index page
    """
    articles = Post.objects.all()
    recent_articles = Post.objects.order_by('-created_at')[:3]
    featured_article = Post.objects.order_by('-views').first()
    return render(request, 'index.html', {'articles': articles,
                                          'recent_articles': recent_articles,
                                          'featured_article': featured_article})


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
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                # Redirect to a success page
                return redirect('') 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            print('Inalid form')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    django_logout(request)
    return redirect('')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            # Redirect to the post detail page
            return redirect('/post/{}'.format(post.pk))
    else:
        form = PostForm()
        
    return render(request, 'create_post.html', {'form': form})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.views += 1
    post.save()
    return render(request, 'post_detail.html', {'post': post})
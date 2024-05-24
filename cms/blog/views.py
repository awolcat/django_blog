from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm, LoginForm, PostForm, CommentsForm
from .models import Post, Comments


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

@login_required
def logout(request):
    django_logout(request)
    return redirect('')

# @login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post = Post(
                
                content=cleaned_data['content'],
                image=cleaned_data['image'],
                author=request.user,
                category=cleaned_data['category']
            )
            post.save()
            # Redirect to the post detail page
            return redirect('/post/{}'.format(post.pk))
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.views += 1
    post.save()
    comments = post.comments.all()
    form = CommentsForm(article_post=post.id)
    
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

def comments(request):
    if request.method == 'POST':
        #data = {'post': request.headers['Referer'].split('/')[4], 'content': request.POST.content}
        request_data = request.POST.copy()
        article_post = int(request.headers['Referer'].split('/')[4])
        request_data['article_post'] = article_post
        form = CommentsForm(request_data, article_post=article_post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_post = Post.objects.get(pk=article_post)
            comment.save()
            # Redirect to the post detail page
            #print(request.headers)
            return redirect(f'/post/{article_post}')
        
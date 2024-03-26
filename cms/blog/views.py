from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Post, Comments
# Create your views here.

def index(request):
    """Index page
    """
    return render(request, 'base.html') 
    
    """HttpResponse(f'Home Page Users: {User.objects.all()} Posts: {Post.objects.all()}')
    """

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    """Index page
    """
    return HttpResponse('<h1>Home Page</h1>')


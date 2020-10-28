from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def population(request):
    
    return render(request, 'population.html')

def work(request):
    
    return render(request, 'work.html')

def corona(request):
    
    return render(request, 'corona.html')

def news(request):
    
    return render(request, 'news.html')
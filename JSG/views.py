from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os

# Create your views here.

def main(request):
    
    return render(request, 'main.html')
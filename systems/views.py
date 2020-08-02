from django.shortcuts import render
from django.conf import settings
# Create your views here.
from .models import *

def home(request):
	return render(request, "home.html")

def about(request):
	return render(request, "about.html")

def contact(request):
	return render(request, "contact.html")

def books(request):
	return render(request, "books.html")

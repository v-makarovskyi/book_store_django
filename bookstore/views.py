from django.shortcuts import render
from django.views.generic import ListView

def home(request):
    return render(request, 'bookstore/home.html')

def single_book(request):
    return render(request, 'bookstore/single_book.html')


# Create your views here.

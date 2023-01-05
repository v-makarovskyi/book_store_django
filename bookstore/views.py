from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

class HomeView(ListView):
    model = Book
    paginate_by = 9
    template_name = 'bookstore/home.html'

def books(request):
    return render(request, 'bookstore/books.html')

def single_book(request):
    return render(request, 'bookstore/single_book.html')

def order_summary(request):
    return render(request, 'bookstore/order_summary.html')


# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

class HomeView(ListView):
    model = Book
    paginate_by = 9
    template_name = 'bookstore/home.html'

class CategoryListView(ListView):
    model = Book
    template_name = 'bookstore/book_list.html'
    
    def get_queryset(self):
        return Book.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'
    template_name = 'bookstore/single_book.html'

def order_summary(request):
    return render(request, 'bookstore/order_summary.html')


# Create your views here.

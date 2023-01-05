from django.urls import path
from .views import HomeView, single_book, order_summary, books

app_name = 'bookstore'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books/',  books, name='books'), 
    path('single/', single_book, name='single_book'),
    path('order/', order_summary, name='order'),
]
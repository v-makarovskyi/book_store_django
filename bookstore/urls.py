from django.urls import path
from .views import HomeView, BookDetailView, CategoryListView, order_summary

app_name = 'bookstore'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/',  CategoryListView.as_view(), name='category_list'), 
    path('<slug:slug>/<slug:book_slug>/', BookDetailView.as_view(), name='single_book'),
    path('order/', order_summary, name='order'),
]
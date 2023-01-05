from django.urls import path
from .views import home, single_book, order_summary

app_name = 'bookstore'

urlpatterns = [
    path('', home, name='home'),
    path('single/', single_book, name='single'),
    path('order/', order_summary, name='order'),
]
from django.urls import path
from .views import HomeView, BookDetailView, CategoryListView

app_name = 'bookstore'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:slug>/',  CategoryListView.as_view(), name='category_list'), 
    path('book/<slug:slug>/<slug:book_slug>/', BookDetailView.as_view(), name='single_book'),
]
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import TemplateView
from .forms import UserLoginForm
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html',
         form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/', views.account_register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

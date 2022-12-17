from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from .views import account_register, account_login, profile
from .forms import UserLoginForm

app_name = 'account'

urlpatterns = [
    path('register/', account_register, name='register'),
    path('login/', account_login , name='login'),
    path('profile/', profile, name='profile_user'),
]
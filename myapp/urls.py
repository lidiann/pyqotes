from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register

urlpatterns = [
     path('login/', auth_views.LoginView.as_view(), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', register, name='register'),
    ]
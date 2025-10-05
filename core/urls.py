from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.home, name='login'),
    path('logout/', views.home, name='logout'),
    path('register/', views.home, name='register'),
]
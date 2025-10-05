from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('recoverpassword/', views.RecoverPassword.as_view(), name='recover_password'),
    path('recoverpassword/done/', views.RecoverPasswordDone.as_view(), name='recover_password_done'),
    path('recoverpassword/<uidb64>/<token>/', views.RecoverPasswordConfirm.as_view(), name='recover_password_confirm'),
    path('recoverpassword/complete/', views.RecoverPasswordComplete.as_view(), name='recover_password_complete'),
]
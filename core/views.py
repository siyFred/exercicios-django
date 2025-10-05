from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout(request):
    return render(request, 'home.html')

def register(request):
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class RecoverPassword(auth_views.PasswordResetView):
    template_name = 'registration/recover_password.html'
    success_url = reverse_lazy('recover_password_done')

class RecoverPasswordDone(auth_views.PasswordResetDoneView):
    template_name = 'registration/recover_password_done.html'

class RecoverPasswordConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'registration/recover_password_confirm.html'
    success_url = reverse_lazy('recover_password_complete')

class RecoverPasswordComplete(auth_views.PasswordResetCompleteView):
    template_name = 'registration/recover_password_complete.html'
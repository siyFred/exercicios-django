from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

def custom_404(request, exception):
    return render(request, 'errorhandlers/404.html', status=404)

def custom_500(request):
    return render(request, 'errorhandlers/500.html', status=500)

def custom_403(request, exception):
    return render(request, 'errorhandlers/403.html', status=403)

class LogoutView(auth_views.LogoutView):
    template_name = 'registration/logout.html'
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
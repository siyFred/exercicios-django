from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy

from core.models import Pessoa

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('profile')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Por favor, faça o login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def custom_404(request, exception):
    return render(request, 'errorhandlers/404.html', status=404)

def custom_500(request):
    return render(request, 'errorhandlers/500.html', status=500)

def custom_403(request, exception):
    return render(request, 'errorhandlers/403.html', status=403)

def listar_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('usuario__first_name')
    context = { 'pessoas': pessoas }
    return render(request, 'listar_pessoas.html', context)
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
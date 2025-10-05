from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    return render(request, 'home.html')

def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
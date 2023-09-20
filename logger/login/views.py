# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.shortcuts import render, redirect


@login_required
def home(request):
    return render(request, 'login/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            login(request, form.get_user())
            return redirect('home')  # Replace 'home' with your desired redirect URL

    else:
        form = AuthenticationForm()
    
    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    # Implement your logout logic here
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            if not User.objects.filter(username=username).exists():
                user = form.save()
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'login/register.html', {'form': form})
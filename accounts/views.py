from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

# User Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Adjust this to your home page URL name
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# User Login View
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Adjust this to your home page URL name
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# User Logout View
def logout(request):
    auth_logout(request)
    return redirect('home')  # Adjust this to your home page URL name

# User Profile Management View
@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after saving
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})




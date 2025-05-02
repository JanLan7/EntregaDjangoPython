from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegisterForm, ProfileEditForm

# Vista para login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Vista para logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Vista para registro de usuario nuevo
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Vista para perfil de usuario
@login_required
def profile_view(request):
    profile = request.user.profile  # Asegúrate de que el perfil esté relacionado con el usuario
    return render(request, 'accounts/profile.html', {'profile': profile})

# Vista para editar perfil de usuario
@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserRegisterForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# Formulario de registro personalizado
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date']

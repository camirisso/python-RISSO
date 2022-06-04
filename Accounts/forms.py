from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.views import generic


# Formulario registro usuarios

class CreacionUsuario(UserCreationForm):
    mail = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput())
    password2 = forms.CharField(label='Repetir contraseña', widget= forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'mail', 'password1', 'password2']
        help_texts = { k: '' for k in fields }

# Formulario edición perfil
class EditProfileForm(UserChangeForm):
    mail = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput())
    password2 = forms.CharField(label='Repetir contraseña', widget= forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'mail', 'password1', 'password2']
        help_texts = { k: '' for k in fields }

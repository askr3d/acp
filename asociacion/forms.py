from .models import Usuario
from django import forms


class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'username', 'contrasenia']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'}),
            'contrasenia': forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'})
        }
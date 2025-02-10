from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UsuarioPromesa

class RegistracionUsuarioForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'readonly':'readonly'}))
    last_name = forms.CharField(label="Apellido",widget=forms.TextInput(attrs={'readonly':'readonly'}))
    username = forms.CharField(label="Usuario",widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="ConfirmaContraseña", widget=forms.PasswordInput)

    class meta:
        model = User
        fields= ['first_name','last_name','username', 'email','password1','password2']
        help_texts ={k:"" for k in fields}

class UsuarioPromesaForm(forms.ModelForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    class Meta:
        model = UsuarioPromesa
#        fields = '__all__'
        fields= ['first_name','last_name','username', 'email']
        help_texts ={k:"" for k in fields}

from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


from .models import   Cultivos, Tierras_Cultivo, Enfermedades, Plagas,GaleriaImagen


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

  
class CultivosForm(forms.ModelForm):
    class Meta:
        model = Cultivos
        fields = '__all__'



class Tierras_CultivoForm(forms.ModelForm):
    class Meta:
        model = Tierras_Cultivo
        fields = '__all__'

class EnfermedadesForm(forms.ModelForm):
    class Meta:
        model = Enfermedades
        fields = '__all__'

class PlagasForm(forms.ModelForm):
    class Meta:
        model = Plagas
        fields = '__all__'

class GaleriaImagenForm(forms.ModelForm):
    class Meta:
        model = GaleriaImagen
        fields = '__all__'
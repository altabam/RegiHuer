from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


from .models import   Cultivos, Suelos, Enfermedades, Plagas,GaleriaImagen, Temperaturas_Variedades_Cultivos, Luz_Variedades_Cultivos, Riego_Cultivo, Variedades_Cultivos,Fecha_Siembra_Variedades_Cultivos

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

        
class Variedades_CultivosForm(forms.ModelForm):
     class Meta:
        model = Variedades_Cultivos
        fields = '__all__'
        widgets = {
            'cultivo': forms.HiddenInput()
        }


class Temperaturas_Variedades_CultivosForm(forms.ModelForm):
    class Meta:
        model = Temperaturas_Variedades_Cultivos
        fields = '__all__'
        widgets = {
            'variedad_cultivo': forms.HiddenInput()
        }
class Luz_Variedades_CultivosForm(forms.ModelForm):
    class Meta:
        model = Luz_Variedades_Cultivos
        fields = '__all__'
        widgets = {
            'variedad_cultivo': forms.HiddenInput()
        }

class Fecha_Siembra_Variedades_CultivosForm(forms.ModelForm):
    class Meta:
        model = Fecha_Siembra_Variedades_Cultivos
        fields = '__all__'
        widgets = {
            'variedad_cultivo': forms.HiddenInput()
        }


class RiegoForm(forms.ModelForm):
    class Meta:
        model = Riego_Cultivo
        fields = '__all__'

class SuelosForm(forms.ModelForm):
    class Meta:
        model = Suelos
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
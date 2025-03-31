from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


from .models import Huerta, Canteros, Cultivos, Cantero_Cultivos, Tierras_Cultivo, Enfermedades, Plagas,GaleriaImagen


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

class HuertaForm(forms.ModelForm):
    class Meta:
        model = Huerta
        fields = '__all__'
        widgets = {
            'hortelano':  forms.Select(attrs = {'option':1} )

        }
    def __init__(self, *args, **kwargs): 
        super(HuertaForm, self).__init__(*args, **kwargs) 
        self.fields['hortelano'].empty_label = None

class CanteroForm(forms.ModelForm):
    class Meta:
        model = Canteros
        fields = '__all__'
        widgets = {
            'huerta': forms.TextInput(attrs={'readonly': 'true'}),
        }
        labels = {
               'nombre': 'Nombre Cantero',
            }
        help_texts = {
               'Nombre': 'Escriba un nombre identificador del Cantero'
            }
        error_messages = {
               'nombre': {
               'max_length': "Nombre solo puede ser de 50 caracteres de largo"
                }
            }
        field_classes = {
      #         'email': EmailCoffeehouseFormField
            },
        localized_fields = '__all__'

    def __init__(self, *args, **kwargs): 
        super(CanteroForm, self).__init__(*args, **kwargs) 
        self.fields['huerta'].empty_label = None
  #      self.fields['huerta'].disabled ='false'


  
class CultivosForm(forms.ModelForm):
    class Meta:
        model = Cultivos
        fields = '__all__'


class Cantero_CultivosForm(forms.ModelForm):
    class Meta:
        model = Cantero_Cultivos
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
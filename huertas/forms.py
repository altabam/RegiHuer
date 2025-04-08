from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


from .models import Huerta, Canteros, Cultivos, Cantero_Cultivos 

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


class Cantero_CultivosForm(forms.ModelForm):
    class Meta:
        model = Cantero_Cultivos
        fields = '__all__'


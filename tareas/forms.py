from django import forms
from django.forms import TextInput
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        exclude = ['fecha_inicial']
        labels = {
            'titulo':'Título', 
            'descripcion':'Descripción',
            'prioridad':'Prioridad',
            'fecha_final':'Fecha final'
        }
        error_messages = {
            'titulo':'Este campo no debe estar vacío'
        }
        widgets = {
            'prioridad':TextInput(attrs={'type':'number', "min":1, 'max':7})
        }
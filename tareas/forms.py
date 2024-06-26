from django import forms
from django.forms import TextInput, DateInput
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'prioridad', 'fecha_final']
        labels = {
            'titulo':'Título', 
            'descripcion':'Descripción',
            'prioridad':'Prioridad',
            'fecha_final':'Fecha final'
        }
        """ error_messages = {
            'titulo':'Este campo no debe estar vacío'
        } """
        widgets = {
            'prioridad':TextInput(attrs={'type':'number', "min":1, 'max':7}),
            'fecha_final':DateInput(format=('%Y-%m-%d'), attrs=({'type':'date'}))
        }
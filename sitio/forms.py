from django import forms
from .models import Biografia, Proyecto, Destacado

class BiografiaForm(forms.ModelForm):
    class Meta:
        model = Biografia
        fields = ['nombre', 'profesion', 'descripcion', 'foto']
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'imagen', 'link']

class DestacadoForm(forms.ModelForm):
    class Meta:
        model = Destacado
        fields = ['titulo', 'subtitulo', 'imagen', 'orden']

        
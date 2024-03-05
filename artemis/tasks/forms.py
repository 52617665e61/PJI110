from django import forms
from .models import Perdido, Encontrado

class PerdidoForm(forms.ModelForm):
    class Meta:
        model = Perdido
        fields = ('especie', 'raca', 'cor', 'tamanho', 'localidade', 'caracteristica', 'tempo', 'contato')

class EncontradoForm(forms.ModelForm):
    class Meta:
        model = Encontrado
        fields = ('especie', 'raca', 'cor', 'tamanho', 'localidade', 'caracteristica', 'tempo', 'contato')
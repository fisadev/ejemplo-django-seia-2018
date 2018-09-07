from django import forms
from sitio.models import Noticia


class FormNoticia(forms.Form):
    titulo = forms.CharField(label="Titulo")
    fecha = forms.DateTimeField(label="Fecha")
    texto = forms.CharField(label='Texto', required=True)


class FormNoticiaMagico(forms.ModelForm):
    class Meta:
        fields = ['titulo', 'fecha', 'texto', 'archivada']
        model = Noticia

from django import forms
from .models import Ciudad, Documento, Subcategoria, Categoria

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre']  # Cambia 'nombre' por el campo que tienes en tu modelo

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['titulo', 'contenido']  # Cambia por los campos que tengas en tu modelo Documento

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = ['nombre']  # Cambia 'nombre' por el campo que tienes en tu modelo

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']  # Cambia 'nombre' por el campo que tienes en tu modelo

class CiudadDocumentoForm(forms.Form):
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), label='Ciudad')
    documento = forms.ModelChoiceField(queryset=Documento.objects.all(), label='Tipo de Documento')
    subcategoria = forms.ModelChoiceField(queryset=Subcategoria.objects.all(), label='Subcategoría')
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')  # Nuevo campo añadido

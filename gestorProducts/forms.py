from django import forms
from .models import Producto, Categoria



class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=200, required=True)

    nombre.widget.attrs.update({'class': 'form-control'})
    descripcion.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=200, required=True)
    precio = forms.IntegerField(required=True)
    stock = forms.IntegerField(required=True)
    categoria = forms.CharField(max_length=50, required=True)

    nombre.widget.attrs.update({'class': 'form-control'})
    descripcion.widget.attrs.update({'class': 'form-control'})
    precio.widget.attrs.update({'class': 'form-control'})
    stock.widget.attrs.update({'class': 'form-control'})
    categoria.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'stock', 'categoria')
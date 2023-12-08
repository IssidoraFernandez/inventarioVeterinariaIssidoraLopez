from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductoForm
from .models import Producto
from django import http
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Producto
from .models import Categoria
from .forms import CategoriaForm

# Create your views here.

def agregarProducto(request):
    form = ProductoForm
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'productosForm.html')
        
    return render(request, 'productosForm.html', {'form': form})


def listarProductos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'listarProductos.html', data)

def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarProductos')  
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editarProducto.html', {'form': form})




def esAdmin(user):
    return user.is_superuser

@user_passes_test(esAdmin)
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return http.HttpResponseRedirect('/listarProductos')


@user_passes_test(esAdmin)
def agregarCategoria(request):
    form = CategoriaForm
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'categoriaForm.html')
        
    return render(request, 'categoriaForm.html', {'form': form})

@user_passes_test(esAdmin)
def listarCategorias(request):
    categorias = Categoria.objects.all()
    data = {
        'categorias': categorias
    }
    return render(request, 'listarCategorias.html', data)

@user_passes_test(esAdmin)
def editarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listarCategorias')  
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'editarCategoria.html', {'form': form})


@user_passes_test(esAdmin)
def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return http.HttpResponseRedirect('/listarCategorias')

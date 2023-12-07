from django.shortcuts import render
from .forms import ProductoForm

# Create your views here.

def agregarProducto(request):
    form = ProductoForm
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'productosForm.html')
        
    return render(request, 'productosForm.html', {'form': form})
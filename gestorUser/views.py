from django import http
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import SignUpForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def personasIndex(request):
    return render(request, 'index.html')

@login_required
def panelAdmin(request):
    if request.user.is_superuser:
        return render(request, 'homeAdmin.html')
    else:
        return render(request, 'homeUser.html')
    

def signUp(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panelAdmin')

    return render(request, 'signUp.html', {'form': form})

def editarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    form = SignUpForm(instance=usuario)

    data = {
        'form': form
    }

    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect('/listarUsuarios')


        data['form'] = form

    return render(request, 'editarUsuario.html', data)


def esAdmin(user):
    return user.is_superuser


@user_passes_test(esAdmin)
def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    data = {
        'usuarios': usuarios
    }
    return render(request, 'listarUsuarios.html', data)


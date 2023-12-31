"""
URL configuration for inventarioVeterinariaIssidoraLopez project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView
from gestorUser.views import *
from gestorProducts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', personasIndex , name='index'), 
    path('cuentas/', include("django.contrib.auth.urls")),
    # path('panelAdmin/',TemplateView.as_view(template_name='home.html'),name='home'),#
    path('panelAdmin/',panelAdmin , name='panelAdmin'),
    path('signUp/',signUp , name='signUp'),
    path('productos/', agregarProducto, name='agregarProductos'),
    path('editarUsuario/<int:id>', editarUsuario, name='editarUsuario'),
    path('listarUsuarios/', listarUsuarios, name='listarUsuarios'),
    path('listarProductos/', listarProductos, name='listarProductos'),
    path('editarProducto/<int:id>/', editarProducto, name='editarProducto'),
    path('eliminarProducto/<int:id>/', eliminarProducto, name='eliminarProducto'),
    path('agregarCategoria/', agregarCategoria, name='agregarCategoria'),
    path('listarCategorias/', listarCategorias, name='listarCategorias'),
    path('eliminarCategoria/<int:id>/', eliminarCategoria, name='eliminarCategoria'),
]

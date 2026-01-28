from django.shortcuts import render, redirect
from .models import Proyecto, Destacado, Biografia
from django.contrib.auth.decorators import login_required
from .forms import BiografiaForm, ProyectoForm, DestacadoForm
from django.contrib.auth import login, logout



def inicio(request):
    proyectos = Proyecto.objects.all()
    destacados = Destacado.objects.order_by('orden')
    biografia = Biografia.objects.first()  # Assuming you want the first biography entry
    return render(request, 'sitio/inicio.html', {
        'proyectos': proyectos, 
        'destacados': destacados,
        'biografia': biografia,
    })

def ver_biografia(request):
    biografia = Biografia.objects.first()
    return render(request, 'sitio/biografia.html', {'biografia': biografia})

def ver_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'sitio/proyectos.html', {'proyectos': proyectos})

def contacto(request):
    return render(request, 'sitio/contacto.html')

@login_required
def panel_admin(request):
    return render(request, 'sitio/panel.html')

@login_required
def editar_biografia(request):
    bio = Biografia.objects.first()
    if request.method == 'POST':
        form = BiografiaForm(request.POST, request.FILES, instance=bio)
        if form.is_valid():
            form.save()
            return redirect('panel')
    else:
        form = BiografiaForm(instance=bio)

    return render(request, 'sitio/editar_biografia.html', {'form': form})

@login_required
def listar_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'sitio/proyectos_listar.html', {'proyectos': proyectos})

@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'sitio/proyectos_form.html', {'form': form, 'accion': 'Crear'})

@login_required
def editar_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('listar_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'sitio/proyectos_form.html', {'form': form, 'accion': 'Editar'})

@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    proyecto.delete()
    return redirect('listar_proyectos')

@login_required
def listar_destacados(request):
    destacados = Destacado.objects.all()
    return render(request, 'sitio/destacados_listar.html', {'destacados': destacados})

@login_required
def crear_destacado(request):
    if request.method == 'POST':
        form = DestacadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_destacados')
    else:
        form = DestacadoForm()
    return render(request, 'sitio/destacados_form.html', {'form': form, 'accion': 'Crear'})

@login_required
def editar_destacado(request, destacado_id):
    destacado = Destacado.objects.get(id=destacado_id)
    if request.method == 'POST':
        form = DestacadoForm(request.POST, request.FILES, instance=destacado)
        if form.is_valid():
            form.save()
            return redirect('listar_destacados')
    else:
        form = DestacadoForm(instance=destacado)
    return render(request, 'sitio/destacados_form.html', {'form': form, 'accion': 'Editar'})

@login_required
def eliminar_destacado(request, destacado_id):
    destacado = Destacado.objects.get(id=destacado_id)
    destacado.delete()
    return redirect('listar_destacados')

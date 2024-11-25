from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import cancion
from .forms import libroform

# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')
def body(request):
    return render(request, 'paginas/body.html')

def index(request):
    index = cancion.objects.all()
    return render(request, 'Musica/index.html', {'index': index})

def crear(request):
        formulario = libroform (request.POST or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        return render(request, 'Musica/crear.html', {'formulario': formulario})

def editar(request, id):  # Aquí recibimos el 'id' desde la URL
    # Obtener el objeto 'cancion' correspondiente al id
    cancion_obj = get_object_or_404(cancion, id=id)

    # Crear el formulario con los datos actuales de la canción
    formulario = libroform(request.POST or None, request.FILES or None, instance=cancion_obj)

    # Si el formulario es válido, guardar los cambios
    if formulario.is_valid():
        formulario.save()
        return redirect('index')  # Redirige al índice después de guardar los cambios

    # Si el formulario no es válido, mostrar el formulario con los datos actuales
    return render(request, 'Musica/editar.html', {'formulario': formulario})

def borrar(request, id):
    cancion_obj = cancion.objects.get(id=id)
    cancion_obj.delete()
    return redirect('index')

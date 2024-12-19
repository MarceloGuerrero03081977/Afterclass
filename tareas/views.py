from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Tarea, Categoria, Nota

# Vista para listar todas las tareas
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

# Vista para ver los detalles de una tarea
def detalle_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    notas = Nota.objects.filter(tarea=tarea)
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea, 'notas': notas})
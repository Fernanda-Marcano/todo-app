from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea
from .forms import TareaForm


def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(to='lista-tarea')
        else:
            return HttpResponse('Error al crear la tarea')
    else:
        form = TareaForm()
        context = {
            'form':form,
        }
        return render(request, 'tarea/crear_tarea.html', context)


def lista_tarea(request):
    form = Tarea.objects.all()
    context = {
        'forms':form,
    }
    return render(request, 'tarea/lista_tarea.html', context)


def editar_tarea(request, id):
    id_tarea = Tarea.objects.get(id=id)
    form = TareaForm(request.POST or None, instance=id_tarea)
    if form.is_valid():
        form.save()
        return redirect(to='lista-tarea')
    else:
        HttpResponse('Error')
    if request.method == 'GET':
        form = TareaForm(instance=id_tarea)
        context = {
            'form':form, 
            'id_tarea':id_tarea,
        }
        return render(request, 'tarea/editar_tarea.html', context)


def eliminar_tarea(request, id):
    try:
        id_tarea = Tarea.objects.get(id=id)
        id_tarea.delete()
        return redirect(to='lista-tarea')
    except Exception as e:
        print(f'Ha ocurrido un error {e}')


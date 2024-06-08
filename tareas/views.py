from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Tarea
from .forms import TareaForm


def crear_tarea(request):
    try:
        if request.method == 'POST':
            form = TareaForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, 'La tarea se ha registrado correctamente')
                return redirect(to='lista-tarea')
            else:
                messages.error(request, 'Ha ocurrido un error con los datos del formulario. Por favor verifique que este correcto')
                return redirect(to='crear-tarea')
        else:
            form = TareaForm()
            context = {
                'form':form,
            }
            return render(request, 'tarea/crear_tarea.html', context)
    except ValueError as e:
        print(f'Error {e}')


def lista_tarea(request):
    try:
        form = Tarea.objects.all()
        context = {
            'forms':form,
        }
        return render(request, 'tarea/lista_tarea.html', context)
    except ValueError as e:
        print(f'Error {e}')


def editar_tarea(request, id):
    try:
        id_tarea = Tarea.objects.get(id=id)
        form = TareaForm(request.POST or None, instance=id_tarea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea editada correctamente')
            return redirect(to='lista-tarea')
        else:
            messages.error(request, 'Ha ocurrido un error')
        if request.method == 'GET':
            form = TareaForm(instance=id_tarea)
            context = {
                'form':form, 
                'id_tarea':id_tarea,
            }
            return render(request, 'tarea/editar_tarea.html', context)
    except ValueError as e:
        print(f'Error {e}')


def detalle_tarea(request, id):
    try:
        id_tarea = Tarea.objects.get(id=id)
        context = {
            'id_tarea':id_tarea
        }
        return render(request, 'tarea/detalle_tarea.html', context)
    except ValueError as e:
        print(f'Ha ocurrido un error {e}')


def eliminar_tarea(request, id):
    try:
        id_tarea = Tarea.objects.get(id=id)
        id_tarea.delete()
        messages.success(request, 'Tarea eliminada correctamente')
        return redirect(to='lista-tarea')
    except ValueError as e:
        print(f'Ha ocurrido un error {e}')


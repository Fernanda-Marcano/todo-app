from django.urls import path
from . import views


urlpatterns = [
    path('crear/', views.crear_tarea, name='crear-tarea'),
    path('lista/', views.lista_tarea, name='lista-tarea'), 
    path('editar/<int:id>/', views.editar_tarea, name='editar-tarea'),
    path('detalle/<int:id>/', views.detalle_tarea, name='detalle-tarea'),
    path('eliminar/<int:id>/', views.eliminar_tarea, name='eliminar-tarea'),
]
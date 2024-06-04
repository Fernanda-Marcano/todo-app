from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'prioridad', 'fecha_inicial')
    list_display = ('titulo', 'descripcion', 'fecha_inicial', 'prioridad')
    list_filter = ('titulo', 'prioridad', 'fecha_inicial')
    date_hierarchy = 'fecha_inicial'
admin.site.register(Tarea, TareaAdmin)


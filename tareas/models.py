from django.db import models
from datetime import date 


class Tarea(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=100, null=False, blank=False, help_text='Escriba el título de la tarea')
    descripcion = models.TextField(verbose_name='Descripción', help_text='Indique una breve descripción de la tarea', null=True, blank=True)
    prioridad = models.IntegerField(verbose_name='Prioridad', help_text='Indique la prioridad de la tarea', default=1)
    fecha_inicial = models.DateField(verbose_name='Fecha Inicial', default=date.today)
    fecha_final = models.DateField(verbose_name='Fecha Final', null=True, blank=True)
    
    class Meta:
        db_table = 'tbl_tarea'
        ordering = ('id', 'titulo')
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
    
    def __str__(self):
        return self.titulo
    
    def clean(self):
        if self.titulo:
            self.titulo = self.titulo.strip().capitalize()
        if self.descripcion:
            self.descripcion = self.descripcion.strip().capitalize()

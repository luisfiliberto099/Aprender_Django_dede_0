from django.db import models
from datetime import datetime


class Tipo(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')

    def __ctr__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']



class empleado(models.Model):
    categoria = models.ManyToManyField(Categoria)
    nombres = models.CharField(max_length=150, verbose_name='Nombres', default='Sin nombres')
    dni = models.CharField(max_length=11, unique=True, verbose_name='Carnet')
    fecha_registro = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    edad = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    genero = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='Avatar/%y/%m/%d', null=True, blank=True)
    curriculum = models.ImageField(upload_to='curriculum/%y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.nombres

    class Meta():
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
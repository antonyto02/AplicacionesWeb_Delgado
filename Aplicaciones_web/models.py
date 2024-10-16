# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Libros(models.Model):
    id_libro = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=40, blank=True, null=True)
    autor = models.CharField(max_length=40, blank=True, null=True)
    categoria = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libros'


class Prestamos(models.Model):
    id_prestamo = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=40, blank=True, null=True)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    estado = models.CharField(max_length=20, blank=True, null=True)
    libro = models.ForeignKey(Libros, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestamos'

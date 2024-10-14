from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=13)

    def __str__(self):
        return self.nombre
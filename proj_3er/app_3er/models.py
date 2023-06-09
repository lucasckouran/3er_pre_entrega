from django.db import models

# Create your models here.
class Curso(models.Model):
    curso = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
	    return f"Curso: {self.curso} - Camada: {self.camada}"

class Estudiante(models.Model):
	nombre = models.CharField(max_length=40)
	apellido = models.CharField(max_length=20)
	email = models.EmailField(max_length=40)
	def __str__(self):
		return f"Nombre: {self.nombre} - Apellido: {self.apellido} - email: {self.email}"

class Profesor(models.Model):
	nombre = models.CharField(max_length=40)
	apellido = models.CharField(max_length=20)
	email = models.EmailField(max_length=40)
	
class Entregable(models.Model):
	nombre = models.CharField(max_length=40)
	fecha_de_entrega = models.DateField()
	entregado = models.BooleanField()
	
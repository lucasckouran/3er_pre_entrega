from django.db import models

# Create your models here.
class Adopcion(models.Model):
    SEXO_CHOICES = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]
    
    nombre = models.CharField(max_length=40)
    sexo = models.CharField(max_length=40, choices=SEXO_CHOICES)

    def __str__(self):
	    return f"Nombre: {self.nombre} - Sexo: {self.sexo}"

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
	
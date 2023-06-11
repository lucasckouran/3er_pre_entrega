from django.shortcuts import render
from app_3er.forms import *
from app_3er.models import *
from django.http import HttpResponse

def index(request):
	return render(request, "app_3er/index.html")

def adopciones(request):
	return render(request, "app_3er/adopciones.html",{"miFormulario":AdopcionFormulario()})

def profesores(request):
	return render(request, "app_3er/profesores.html")

def estudiantes(request):
	return render(request, "app_3er/estudiantes.html")

def entregables(request):
	return render(request, "app_3er/entregables.html")

#def cursoformulario(request):
	if request.method == "POST":
		miFormulario = CursoFormulario(request.POST)
		print(miFormulario)

		if miFormulario.is_valid():
			informacion = miFormulario.cleaned_data
			curso = Curso(curso = informacion["curso"], camada = informacion["camada"])
			curso.save()
			return render(request,"app_3er/index.html")
	
	else:
		miFormulario = CursoFormulario()

	return render(request, "app_3er/cursoformulario.html",{"miFormulario":miFormulario})

def adopcionformulario(request):
	if request.method == "POST":
		miFormulario = AdopcionFormulario(request.POST)
		print(miFormulario)

		if miFormulario.is_valid():
			informacion = miFormulario.cleaned_data
			adopcion = Adopcion(nombre = informacion["nombre"], sexo = informacion["sexo"])
			adopcion.save()
			return render(request,"app_3er/index.html")
	
	else:
		miFormulario = AdopcionFormulario()

	return render(request, "app_3er/adopciones.html",{"miFormulario":miFormulario})

def estudianteformulario(request):
	if request.method == "POST":
		miFormulario = EstudianteFormulario(request.POST)
		print(miFormulario)

		if miFormulario.is_valid():
			informacion = miFormulario.cleaned_data
			estudiante = Estudiante(nombre = informacion["nombre"], apellido = informacion["apellido"],email = informacion["email"])
			estudiante.save()
			return render(request,"app_3er/index.html")
	
	else:
		miFormulario = EstudianteFormulario()

	return render(request, "app_3er/estudianteformulario.html",{"miFormulario":miFormulario})

def entregableformulario(request):
	if request.method == "POST":
		miFormulario = EntregableFormulario(request.POST)
		print(miFormulario)

		if miFormulario.is_valid():
			informacion = miFormulario.cleaned_data
			estudiante = Entregable(nombre = informacion["nombre"], fecha_de_entrega = informacion["fecha_de_entrega"],entregado = informacion["entregado"])
			estudiante.save()
			return render(request,"app_3er/index.html")
	
	else:
		miFormulario = EntregableFormulario()

	return render(request, "app_3er/entregableformulario.html",{"miFormulario":miFormulario})


def busquedacamada(request):
	return render(request, "app_3er/busquedacamada.html")


def buscar(request):
	if request.GET['camada']:
		camada = request.GET['camada']
		cursos = Curso.objects.filter(camada__icontains=camada)
		

		return render(request, "app_3er/resultadobusqueda.html", {"cursos":cursos, "camada":camada})
	
	else:
		respuesta = "No enviaste datos"

	return HttpResponse(respuesta)
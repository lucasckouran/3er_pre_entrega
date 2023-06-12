from django.shortcuts import render
from app_3er.forms import *
from app_3er.models import *
from django.http import HttpResponse

def index(request):
	return render(request, "app_3er/index.html")

def adopciones(request):
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
	# return render(request, "app_3er/adopciones.html")


def profesores(request):
	return render(request, "app_3er/profesores.html")

def adoptantes(request):
	if request.method == "POST":
		miFormulario = AdoptanteFormulario(request.POST)
		print(miFormulario)

		if miFormulario.is_valid():
			informacion = miFormulario.cleaned_data
			adoptante = Adoptante(nombre = informacion["nombre"], apellido = informacion["apellido"],email = informacion["email"])
			adoptante.save()
			return render(request,"app_3er/index.html")
	
	else:
		miFormulario = AdoptanteFormulario()

	return render(request, "app_3er/adoptantes.html",{"miFormulario":miFormulario})
	


def entregables(request):
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

	return render(request, "app_3er/entregables.html",{"miFormulario":miFormulario})



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


def busquedagato(request):
	return render(request, "app_3er/busquedagato.html")


def buscar(request):
	if request.GET['nombre']:
		nombre = request.GET['nombre']
		sexo = Adopcion.objects.filter(nombre__icontains=nombre)
		

		return render(request, "app_3er/resultado_busqueda_gato.html", {"nombre":nombre, "sexo":sexo})
	
	else:
		respuesta = "No enviaste datos"

	return HttpResponse(respuesta)
	
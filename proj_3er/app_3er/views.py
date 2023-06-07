from django.shortcuts import render

def index(request):
	return render(request, "app_3er/index.html")

def cursos(request):
	return render(request, "app_3er/cursos.html")

def profesores(request):
	return render(request, "app_3er/profesores.html")

def estudiantes(request):
	return render(request, "app_3er/estudiantes.html")

def entregables(request):
	return render(request, "app_3er/entregables.html")
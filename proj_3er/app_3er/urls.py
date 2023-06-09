from django.urls import path
from app_3er import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('cursos/', views.cursos, name = 'curso'),
	path('profesores/', views.profesores, name = 'profesor'),
	path('estudiantes/', views.estudiantes, name = 'estudiante'),
	path('entregables/', views.entregables, name = 'entregable'),
    path('cursoformulario/',views.cursoformulario, name='cursoformulario'),
    path('estudianteformulario/',views.estudianteformulario, name='estudianteformulario'),
    path('entregableformulario/',views.entregableformulario, name='entregableformulario')
]
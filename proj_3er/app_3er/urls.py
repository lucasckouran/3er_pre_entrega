from django.urls import path
from app_3er import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('adopciones/', views.adopciones, name = 'adopciones'),
	path('profesores/', views.profesores, name = 'profesor'),
	path('estudiantes/', views.estudiantes, name = 'estudiante'),
	path('entregables/', views.entregables, name = 'entregable'),
    path('adopcionformulario/',views.adopcionformulario, name='adopcionformulario'),
    path('estudianteformulario/',views.estudianteformulario, name='estudianteformulario'),
    path('entregableformulario/',views.entregableformulario, name='entregableformulario'),
    path('busquedacamada/', views.busquedacamada, name='busquedacamada'),
    path('buscar/', views.buscar)
]
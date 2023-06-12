from django.urls import path
from app_3er import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('adopciones/', views.adopciones, name = 'adopciones'),
	path('profesores/', views.profesores, name = 'profesor'),
	path('adoptantes/', views.adoptantes, name = 'adoptantes'),
	path('entregables/', views.entregables, name = 'entregable'),
    path('busquedagato/', views.busquedagato, name='busquedagato'),
    path('buscar/', views.buscar)
]
from django.urls import path
from app_3er import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('adopciones/', views.adopciones, name = 'adopciones'),
	path('insumos/', views.insumos, name = 'insumos'),
	path('adoptantes/', views.adoptantes, name = 'adoptantes'),
	path('entregables/', views.entregables, name = 'entregable'),
    path('busquedagato/', views.busquedagato, name='busquedagato'),
    path('buscar/', views.buscar)
]
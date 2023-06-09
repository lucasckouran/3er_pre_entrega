from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class EntregableFormulario(forms.Form):
	nombre = forms.CharField(max_length=40)
	fecha_de_entrega = forms.DateField()
	entregado = forms.BooleanField()
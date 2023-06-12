from django import forms

class AdopcionFormulario(forms.Form):
    SEXO_CHOICES = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]
    
    nombre = forms.CharField(max_length=40)
    sexo = forms.ChoiceField(choices=SEXO_CHOICES)

class AdoptanteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class EntregableFormulario(forms.Form):
	nombre = forms.CharField(max_length=40)
	fecha_de_entrega = forms.DateField()
	entregado = forms.BooleanField()
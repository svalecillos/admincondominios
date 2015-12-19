from django import forms
from .models import Condominio

class CondominioForm(forms.Form):
	class Meta:
		model = Condominio
		#fields = ('usuario', 'cedula', 'nombre', 'apellido', 'correo', 'password')
		widgets = {
			'nombre_edificacion' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre de usuario',
				})}

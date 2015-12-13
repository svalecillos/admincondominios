from django import forms
from .models import Usuario

class RegistrarUsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ('usuario', 'cedula', 'nombre', 'apellido', 'correo', 'password')
		widgets = {
			'usuario' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre de usuario',
				'id': 'inputName'
				}),
			'cedula' : forms.NumberInput(attrs = 
				{
				'type' : 'number',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa tu cedula',
				'id': 'inputCedula'
				}),
			'nombre' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control',
				'placeholder' : 'Ingresa tu nombre',
				'id': 'inputNombre'
				}),
			'apellido' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control',
				'placeholder' : 'Ingresa tu apellido',
				'id': 'inputApellido'
				}),
			'correo' : forms.EmailInput(attrs = 
				{
				'type' : 'email',
				'class' : 'form-control',
				'placeholder' : 'Ingresa tu correo',
				'id': 'inputEmail'
				}),
			'password' : forms.PasswordInput(attrs = 
				{
				'type' : 'password',
				'class' : 'form-control',
				'placeholder' : 'Ingresa tu clave',
				'id': 'inputPassword'
				})
		}

class LoginForm(forms.Form):

	usuario = forms.CharField(max_length=50, 
				widget = forms.TextInput(attrs = {
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'Ingresa tu nombre de usuario',
					'id': 'inputName'
					}))
	password = forms.CharField(max_length=50,
	 			widget = forms.PasswordInput(attrs = {
	 				'type' : 'password',
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingresa tu clave',
	 				'id': 'inputPassword'
	 				}))
from django import forms
from .models import Usuario

class LoginForm(forms.Form):

	usuario = forms.CharField(max_length=50, 
				widget = forms.TextInput(attrs = {
					'type' : 'text',
					'class' : 'form-control form-block',
					'placeholder' : 'Ingresa tu nombre de usuario',
					'id': 'inputUsuario',
					'required' : ''
					}))
	password = forms.CharField(max_length=50,
	 			widget = forms.PasswordInput(attrs = {
	 				'type' : 'password',
	 				'class' : 'form-control form-block',
	 				'placeholder' : 'Ingresa tu clave',
	 				'id': 'inputPassword',
	 				'required' : ''
	 				}))


class Contact_form(forms.Form):

	nombre = forms.CharField(max_length=50, 
				widget = forms.TextInput(attrs = {
					'id': 'inputName',
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'Ingresa tu nombre',
					'required' : ''					
					}))

	email = forms.CharField(max_length=50,
	 			widget = forms.EmailInput(attrs = {
	 				'id': 'inputEmail',
	 				'type' : 'email',
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingresa tu correo',
	 				'required' : ''	 				
	 				}))

	mensaje = forms.CharField(max_length=500,
	 			widget = forms.Textarea(attrs = {
	 				'id': 'inputMensaje',
	 				'type' : 'text',
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingresa tu mensaje',
	 				'Rows' : '4',
	 				'required' : ''	 				
	 				}))

class RegistrarUsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ('usuario', 'cedula', 'nombre', 'apellido', 'correo', 'rol', 'password')
		widgets = {
			'usuario' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre de usuario',
				'id': 'inputUsuario'
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
			'rol' : forms.NumberInput(attrs = 
				{
				'type' : 'number',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa tu rol',
				'id': 'inputRol'
				}),
			'password' : forms.PasswordInput(attrs = 
				{
				'type' : 'password',
				'class' : 'form-control',
				'placeholder' : 'Ingresa tu clave',
				'id': 'inputPassword'
				})
		}

# class ModificarUsuarioForm(forms.ModelForm):

# 	class Meta:
# 		model = Usuario
# 		fields = ('usuario', 'cedula', 'nombre', 'apellido', 'correo', 'telefono_habitacion', 'telefono_movil', 'numero_vivienda', 'password')
# 		widgets = {
# 			'usuario' : forms.TextInput(attrs = 
# 				{
# 				'type' : 'text',
# 				'class' : 'form-control', 
# 				'value' : '{{ user.usuario }}',
# 				'name' : 'usuario',
# 				'id': 'inputUsuario',
# 				'required' : ''
# 				}),
# 			'cedula' : forms.NumberInput(attrs = 
# 				{
# 				'type' : 'number',
# 				'class' : 'form-control', 
# 				'value' : '{{ user.cedula }}',
# 				'name' : 'cedula',
# 				'id': 'inputCedula',
# 				'required' : ''
# 				}),
# 			'nombre' : forms.TextInput(attrs = 
# 				{
# 				'type' : 'text',
# 				'class' : 'form-control',
# 				'value' : '{{ user.nombre }}',
# 				'name' : 'nombre',
# 				'id': 'inputNombre',
# 				'required' : ''
# 				}),
# 			'apellido' : forms.TextInput(attrs = 
# 				{
# 				'type' : 'text',
# 				'class' : 'form-control',
# 				'value' : '{{ user.apellido }}',
# 				'name' : 'apellido',
# 				'id': 'inputApellido',
# 				'required' : ''
# 				}),
# 			'correo' : forms.EmailInput(attrs = 
# 				{
# 				'type' : 'email',
# 				'class' : 'form-control',
# 				'value' : '{{ user.correo }}',
# 				'name' : 'correo',
# 				'id': 'inputEmail',
# 				'required' : ''
# 				}),
# 			'telefono_habitacion' : forms.TextInput(attrs = 
# 				{
# 				'type' : 'number',
# 				'class' : 'form-control', 
# 				'value' : '{{ user.telefono_habitacion }}',
# 				'name' : 'telefono_habitacion',
# 				'id': 'inputTelefono_habitacion'
# 				}),
# 			'telefono_movil' : forms.TextInput(attrs = 
# 				{
# 				'type' : 'number',
# 				'class' : 'form-control', 
# 				'value' : '{{ user.telefono_movil }}',
# 				'name' : 'telefono_movil',
# 				'id': 'inputTelefono_movil',
# 				'required' : ''
# 				}),
# 			'numero_vivienda' : forms.TextInput(attrs = 
# 				{
# 				'type' : 'text',
# 				'class' : 'form-control', 
# 				'value' : '{{ user.numero_vivienda }}',
# 				'name' : 'numero_vivienda',
# 				'id': 'inputNumero_vivienda',
# 				'required' : ''
# 				})
# 		}
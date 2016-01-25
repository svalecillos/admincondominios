from django import forms
from .models import *
from apps.usuarios.models import *

# Lo intente pero que va es demaciado tedioso

class RegistrarPagoForm(forms.Form):

	banco = forms.CharField(max_length=50, 
				widget = forms.TextInput(attrs = {
					'id': 'inputBanco',
					'type' : 'text',
					'class' : 'form-control input-lg',
					'required' : ''					
					}))

	tipoPago = forms.ChoiceField(
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

class RegistrarCondominioForm(forms.ModelForm):

	class Meta:
		model = Condominio
		fields = ('condominio','rif','telefono','correo','parroquia',
			'ciudad','avenidaCalle','urbanizacionSector','tipoEdificacion','nombreEdificacion')
		widgets = {
			'condominio' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre de condomino',
				'id': 'condominio',
				'required':'required'
				}),
			'rif' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un rif',
				'id': 'rif',
				'required':'required'
				}),
			'telefono' : forms.TextInput(attrs = 
				{
				'class' : 'form-control',
				'placeholder' : 'Ingresa un telefono de contacto',
				'id': 'telefono',
				'required':'required'
				}),
			'correo' : forms.TextInput(attrs = 
				{
				'type' : 'mail',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un correo',
				'id': 'correo',
				'required':'required'
				}),
			'parroquia': forms.Select(attrs=
				{
				'class': 'form-control',
				'id': 'parroquia',
				'required':'required'
				}),
			'ciudad': forms.Select(attrs=
				{
				'class': 'form-control',
				'id': 'ciudad',
				'required':'required'
				}),
			'avenidaCalle' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa una avenida o calle',
				'id': 'avenidaCalle',
				'required':'required'
				}),
			'urbanizacionSector' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa una urbanizacion o sector',
				'id': 'urbanizacionSector',
				'required':'required'
				}),
			'tipoEdificacion': forms.Select(attrs=
				{
				'class': 'form-control',
				'id': 'tipoedificacion',
				'required':'required'
				}),
			'nombreEdificacion' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa el nombre de la edificacion',
				'id': 'nombreedificacion',
				'required':'required'
				})	
		}

class ActualizarCondominioForm(forms.Form):

	condominio = forms.CharField(max_length=50, 
				widget = forms.TextInput(attrs = {
					'id': 'condominio',
					'type' : 'text',
					'class' : 'form-control input-lg',
					'required' : ''					
					}))

	correo = forms.CharField(max_length=50,
	 			widget = forms.EmailInput(attrs = {
	 				'id': 'inputEmail',
	 				'type' : 'email',
	 				'class' : 'form-control',
	 				'required' : ''	 				
	 				}))


class RegistrarProveedorForm(forms.ModelForm):

	class Meta:
		model = Proveedor
		fields = ('condominio','proveedor','rif','correo','telefono','telefono')
		widgets = {
			'proveedor' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre de proveedor',
				'id': 'proveedor'
				}),
			'rif' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un rif',
				'id': 'rif'
				}),
			'telefono' : forms.TextInput(attrs = 
				{
				'type' : 'mail',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un telefono',
				'id': 'telefono'
				}),			
			'correo' : forms.TextInput(attrs = 
				{
				'type' : 'mail',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un correo',
				'id': 'correo'
				}),
			'condominio': forms.Select(attrs=
				{
				'class': 'form-control',
				'id': 'condominio'
				}),			
		}

class RegistrarServicioMensualForm(forms.ModelForm):

	class Meta:
		model = ServicioMensual
		fields = ('condominio','proveedor','servicioMensual','estatus')
		widgets = {
			'proveedor' : forms.Select(attrs = 
				{
				'class' : 'form-control', 
				'id': 'proveedor'
				}),
			'condominio': forms.Select(attrs=
				{
				'class': 'form-control',
				'id': 'condominio'
				}),
			'servicioMensual' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre para el servicio',
				'id': 'servicioMensual'
				}),
		}	

class RegistrarServicioEspecialForm(forms.ModelForm):
	class Meta:
		model = ServicioEspecial
		fields = ('condominio','proveedor','servicioEspecial','estatus')
		widgets = {
			'proveedor' : forms.Select(attrs = 
				{
				'class' : 'form-control', 
				'id': 'proveedor'
				}),
			'condominio': forms.Select(attrs=
				{
				'class': 'form-control',
				'id': 'condominio'
				}),
			'servicioEspecial' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre para el servicio',
				'id': 'servicioEspecial'
				}),
		}

class CostoServicioEspecialRegistrarForm(forms.ModelForm):
	class Meta:
		model = CostoServicioEspecial
		fields = ('costo','condominio','servicioEspecial')
		widgets = {
			'condominio': forms.Select(attrs=
				{
				'class': 'form-control',
				'id': 'condominio'
				}),
			'servicioEspecial' : forms.Select(attrs = 
				{
				'class' : 'form-control',
				'id': 'servicioEspecial'
				}),
			'costo' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un costo',
				'id': 'costo'
				}),
		}

class CostoServicioMensualRegistrarForm(forms.ModelForm):
	class Meta:
		model = CostoServicioMensual
		fields = ('costo','condominio','servicioMensual')
		widgets = {
			'condominio': forms.Select(attrs=
				{
				'class': 'form-control',
				'id': 'condominio'
				}),
			'servicioEspecial' : forms.Select(attrs = 
				{
				'class' : 'form-control',
				'id': 'servicioMensual'
				}),
			'costo' : forms.TextInput(attrs = 
				{
				'type' : 'text',
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un costo',
				'id': 'costo'
				}),
		}

class RegistrarTipoEdificacionForm(forms.ModelForm):
	class Meta:
		model = TipoEdificacion
		fields = ('edificacion',)
		widgets = {
			'edificacion': forms.TextInput(attrs=
				{
				'class': 'form-control',
				'id': 'edificacion'
				}),
		}					

class UsuarioRegistrarForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('nombre','apellido','cedula')
		widgets = {
			'nombre': forms.TextInput(attrs=
				{
				'class': 'form-control',
				'id': 'nombre',
				'placeholder' : 'Nombre del usuario',
				}),
			'apellido': forms.TextInput(attrs=
				{
				'class': 'form-control',
				'id': 'nombre',
				'placeholder' : 'Apellido del usuario',
				}),
			'cedula': forms.TextInput(attrs=
				{
				'class': 'form-control',
				'id': 'nombre',
				'placeholder' : 'Cedula del usuario',
				}),			
		}				
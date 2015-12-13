from django import forms


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
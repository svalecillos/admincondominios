from django.shortcuts import render
#from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import Contact_form
		
def index(request):
	
	if request.method == 'POST':
		formulario_contacto = Contact_form(request.POST)
		if formulario_contacto.is_valid():
			asunto = 'Nuevo mensaje desde la pagina web Administradora JJ24-30'
			mensaje = """%s | %s

			%s"""%(formulario_contacto.cleaned_data['nombre'],formulario_contacto.cleaned_data['email'],formulario_contacto.cleaned_data['mensaje'])
			mail = EmailMessage(asunto, mensaje, destinatario)
			mail.send()
		return render(request,'index.html',{'email_success' : mensaje})
	else:
		formulario_contacto = Contact_form()

	return render(request,'index.html',{'Contact_form' : formulario_contacto})

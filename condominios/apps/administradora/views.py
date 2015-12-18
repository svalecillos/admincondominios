from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .forms import Contact_form
		
def index(request):
	
	formulario_contacto = Contact_form()
	return render(request,'index.html',{'Contact_form' : formulario_contacto})

def envio_correo(request):
	if request.is_ajax():
		asunto = 'Nuevo mensaje desde la pagina web Administradora JJ24-30'
		mensaje = """%s | %s

%s"""%(request.POST['inputName'], request.POST['inputEmail'], request.POST['inputMensaje'])
		remitente = 'correo@gmail.com'
		destinatario = ['correo@gmail.com']
		mail = EmailMessage(asunto, mensaje, remitente, destinatario)
		mail.send(fail_silently=False)
		return HttpResponse(' ')

	else:
		return redirect('/')

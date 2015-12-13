from django.shortcuts import render_to_response, RequestContext
from .models import Estados, Municipios, Parroquias
# Create your views here.
def index(request):
	#estados=Estados.objects.all()
	#municipios=Municipios.objects.all()
	#parroquias=Parroquias.objects.all()


	return render_to_response('index.html', context=RequestContext(request))
	#print (estados, municipios, parroquias)
	#return render(request, '../../condominio/index.html',{'estados': estados, 'municipios': municipios, 'parroquias' : parroquias})
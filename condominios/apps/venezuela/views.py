from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from .models import Ciudad, Estado, Municipio, Parroquia
import json

def geo(request, type = None, parent_id = None):

    #if not request.is_ajax():
     #   return HttpResponseBadRequest('<h1>%s</h1>' % 'bad request')

    # para testear el efecto loading
    #time.sleep(1);

    locations = {

    ###################################################################
    #    Localidad => [modelo, modelo padre, foreignkey, parent type] #
    ###################################################################
        'estado' : [Estado],
        'ciudad' : [Ciudad, Estado, 'estado_id', 'estado'],
        'municipio' : [Municipio, Estado, 'estado_id', 'estado'],
        'parroquia' : [Parroquia, Municipio, 'municipio_id', 'municipio']
    }

    location_exists = False

    if parent_id != None:
        location_exists = (locations[type][2].objects.filter(id = parent_id).count() > 0)
    else:
        location_exists = (locations[type][0].objects.count() > 0)

    if not location_exists:
        return HttpResponseBadRequest('Identificador invalido')

    data_fields = {
        'estado' : ('id', 'estado'),
        'ciudad' : ('id', 'ciudad'),
        'municipio' : ('id', 'municipio'),
        'parroquia' : ('id', 'parroquia')
    }

    extra_where = None

    if parent_id != None:
        extra_where = ['%s = %d' % (locations[type][2], int(parent_id))]

    location_result = locations[type][0].objects.extra(where = extra_where).values(*data_fields[type]).order_by('id')

    if not location_result.count() > 0:
        return HttpResponseNotFound(json.dumps({'error' : 'empty'}))

    data = {
        'parent' : None,
        'data' : list(location_result)
    }

    if parent_id != None:
        data['parent'] = {
            'id' : parent_id,
            'type' : locations[type][3]
        }

    output = json.dumps(data)

    return HttpResponse(output, content_type = 'application/json')
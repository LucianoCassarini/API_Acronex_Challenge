from msilib.schema import Class
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from maquinaria_API.models import Maquina
from django.http import JsonResponse
from django.forms import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import urllib.request

# Create your views here.

#*--------- Consultar ultimo punto conocido ------------
def ultimoPuntoConocido(request, id):
    maquina = get_object_or_404(Maquina, pk=id)
    if maquina:
        endpoint = 'https://wrk.acronex.com/api/challenge/last/'+str(id)+'/'
        peticion = urllib.request.Request(endpoint,
                                        data=None,
                                        headers={
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                                            }
        )
        respuesta = urllib.request.urlopen(peticion)
        cuerpo_respuesta = respuesta.read()
        # Procesamos la respuesta json
        json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
        datos = JsonResponse(json_respuesta)
    else:
        datos={'message': 'No se encontraron maquinarias....'}
    
    return datos

#! --------- Administrar Bajas -----------
class AdminBajas(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):  #*Este metodo se ejecuta cuando hacemos una petición
        return super().dispatch(request, *args, **kwargs)

    def put(self, request, id):
        jd = json.loads(request.body)
        maquinaria = list(Maquina.objects.filter(id=id).values())
        if len(maquinaria)>0:
            maquina = Maquina.objects.get(id=id)
            maquina.nombre=jd['nombre']
            maquina.clase=jd['clase']
            maquina.empresa=jd['empresa']
            maquina.dado_de_baja=jd['dado_de_baja']
            maquina.save()
            datos={'message': 'Success'}
        else:
            datos={'message': 'No se encontraron maquinas....'}
        return JsonResponse(datos)
    


class MaquinaView(View):
        
    #!--------- METODO PARA SALTARNOS LA VALIDACIÓN CSRF ---------
    #Como estamos trabajando sin un cliente usamos este metodo para saltarnos la validación
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):  #*Este metodo se ejecuta cuando hacemos una petición
        return super().dispatch(request, *args, **kwargs)
    
    #!----------  Realizar búsquedas de máquinas ------------
    def get(self, request):
        print(request)
        if('nombre' in request.GET):
            maquinaria = Maquina.objects.filter(nombre= request.GET['nombre']) #Buscar por nombre
        elif('clase' in request.GET):
            maquinaria = Maquina.objects.filter(clase= request.GET['clase'])
        else:
            maquinaria = Maquina.objects.all()
        return JsonResponse(list(maquinaria.values()), safe=False)  #false dice que vamos a devolver un array no un solo objeto
    
    #*--------- Dar de alta una nueva máquina ---------
    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Maquina.objects.create(nombre=jd['nombre'], clase=jd['clase'], empresa=jd['empresa'])
        datos={'message': 'Success'}
        return JsonResponse(datos)
    

class MaquinaDetailView(View):
        
    #!--------- METODO PARA SALTARNOS LA VALIDACIÓN CSRF ---------
    #Como estamos trabajando sin un cliente usamos este metodo para saltarnos la validación
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):  #*Este metodo se ejecuta cuando hacemos una petición
        return super().dispatch(request, *args, **kwargs)
    
    
    # def get(self, request, id):
    #     maquinaria = Maquina.objects.get(pk=id)
    #     return JsonResponse(model_to_dict(maquinaria))  #false dice que vamos a devolver un array no un solo objeto
    
    
    #*--------- Consultar una máquina existente por ID  ---------
    def get(self, request, id=0):
        if (id>0):
            maquinarias=list(Maquina.objects.filter(id=id).values())
            if len(maquinarias)>0:
                maquinaria = maquinarias[0]
                datos={'message': 'Success', 'maquinarias':maquinaria}
            else:
                datos={'message': 'Maquinaria no encontrada....'}
            return JsonResponse(datos)
        else:
            #? Listo las Maquinas a través del ORM de django
            maquinarias = list(Maquina.objects.values())
            
            if len(maquinarias)>0:
                datos={'message': 'Success', 'maquinarias':maquinarias}
            else:
                datos={'message': 'No se encontraron maquinarias....'}
            return JsonResponse(datos)
        
        
    
    #*--------- Actualizar la información de una máquina ---------
    def put(self, request, id):
        jd = json.loads(request.body)
        maquinaria = list(Maquina.objects.filter(id=id).values())
        if len(maquinaria)>0:
            maquina = Maquina.objects.get(id=id)
            maquina.nombre=jd['nombre']
            maquina.clase=jd['clase']
            maquina.empresa=jd['empresa']
            maquina.save()
            datos={'message': 'Success'}
            #maquina.dado_de_baja=jd['dado_de_baja']
        else:
            datos={'message': 'No se encontraron maquinas....'}
        return JsonResponse(datos)
    
    
    
    #*--------- ELIMINAR ---------
    def delete(self, request, id):
        maquinarias=list(Maquina.objects.filter(id=id).values())
        if len(maquinarias) > 0:
            Maquina.objects.filter(id=id).delete()
            datos={'message': 'Success'}
        else:
            datos={'message': 'Maquinaria no encontrada....'} 
        return JsonResponse(datos)




# if __name__ == '__main__':
#     ultimoPuntoConocido(1)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import CategoriaSerializer, CrearCategoriaSerializer, PruebaSerializer
from .models import Categoria
from rest_framework import status

@api_view(http_method_names=['GET','POST'])
def inicio(request:Request):
    print(request.data)
    return Response(data={
        'message':'Endpoint de un decorador'
    })

class PruebaView(ListAPIView):
    # en cualquiera de las clases genericas se necesita declarar los atributos queryset, serializer_class
    queryset=[{
        'nombre':'franco',
        'apellido':'rojas'
    }]
    serializer_class=PruebaSerializer

class CategoriasView(ListAPIView):
    queryset=Categoria.objects.all()
    serializer_class=CategoriaSerializer
    def get(self,request):
        categorias=self.get_queryset()
        categoriaSerializada= self.serializer_class(instance=categorias,many=True)
        return Response(data={
            'message':'Las categorias son',
            'content':categoriaSerializada.data
        },status=status.HTTP_200_OK)

class CrearCategoriasView(CreateAPIView):
    queryset=Categoria.objects.all()
    serializer_class=CrearCategoriaSerializer
    def post(self,request:Request):
        body= request.data
        instanciaSerializador=self.serializer_class(data=body)
        validacion=instanciaSerializador.is_valid(raise_exception=True)
        if validacion== True:
            instanciaSerializador.save()
            
            return Response(data=instanciaSerializador.data, status=status.HTTP_201_CREATED)


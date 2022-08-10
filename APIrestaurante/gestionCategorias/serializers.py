from dataclasses import field
from rest_framework import serializers
from.models import Categoria

class PruebaSerializer(serializers.Serializer):
    nombre=serializers.CharField(max_length=40)
    apellido=serializers.CharField(max_length=40)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'

class CrearCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'
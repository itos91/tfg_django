"""
Book: Building RESTful Python Web Services
Chapter 3: Improving and adding authentication to an API with Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework import serializers
from encargos.models import Encargo
from encargos.models import Producto
from encargos.models import Detalle_Encargo
from django.contrib.auth.models import User


class UserEncargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Encargo
        fields = (
            'url',
            'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    encargos = UserEncargoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'url', 
            'pk',
            'username',
            'encargos',
            'password'
        )

class EncargoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Encargo
        fields = (
            'url',
            'pk',
            'created',
            'completado'
    )


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    localizacion = serializers.ChoiceField(choices=Producto.AREAS)
    area_description = serializers.CharField(source='get_area_display', read_only=True)
    class Meta:
        model = Producto
        fields = (
            'url',
            'pk',
            'name',
            'localizacion',
            'area_description',
        )

class Detalle_EncargoSerializer(serializers.ModelSerializer):
    localizacion_producto = ProductoSerializer(many=True, read_only=True)
    encargo_completado = EncargoSerializer(many=True, read_only=True)
    class Meta:
        model = Detalle_Encargo
        fields = (
            'url',
            'pk',
            'encargo',
            'producto',
            'cantidade',
            'localizacion_producto',
            'encargo_completado'
        )
        







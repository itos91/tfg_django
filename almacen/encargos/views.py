"""
Book: Building RESTful Python Web Services
Chapter 3: Improving and adding authentication to an API with Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from encargos.models import Encargo
from encargos.models import Producto
from encargos.models import Detalle_Encargo
from encargos.serializers import EncargoSerializer
from encargos.serializers import ProductoSerializer
from encargos.serializers import Detalle_EncargoSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from encargos.serializers import UserSerializer
from rest_framework import permissions
from encargos.permissions import IsOperarioOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class EncargoList(generics.ListCreateAPIView):
    queryset = Encargo.objects.all()
    serializer_class = EncargoSerializer
    name = 'encargo-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOperarioOrReadOnly,
        )
    def perform_create(self, serializer):
        # Pass an additional owner field to the create method
        # To Set the owner to the user received in the request
        serializer.save(operario=self.request.user)


class EncargoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Encargo.objects.all()
    serializer_class = EncargoSerializer
    name = 'encargo-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOperarioOrReadOnly)


class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    name = 'producto-list'


class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    name = 'producto-detail'
    

class Detalle_EncargoList(generics.ListCreateAPIView):
    queryset = Detalle_Encargo.objects.all()
    serializer_class = Detalle_EncargoSerializer
    name = 'detalle_encargo-list'


class Detalle_EncargoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detalle_Encargo.objects.all()
    serializer_class = Detalle_EncargoSerializer
    name = 'detalle_encargo-detail'
    

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'productos': reverse(ProductoList.name, request=request),
            'detalle_encargo': reverse(Detalle_EncargoList.name, request=request),
            'encargos': reverse(EncargoList.name, request=request),
            'users': reverse(UserList.name, request=request),
            })

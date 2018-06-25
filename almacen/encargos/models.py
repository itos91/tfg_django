"""
Book: Building RESTful Python Web Services
Chapter 3: Improving and adding authentication to an API with Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.db import models

class Encargo(models.Model):

    operario = models.ForeignKey(
        'auth.User',
        related_name='encargo',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class Producto(models.Model):
    AREA1 = '1'
    AREA2 = '2'
    AREAS = (
        (AREA1, 'Area 1'),
        (AREA2, 'Area 2'),
    )
    name = models.CharField(max_length=50)
    localizacion = models.CharField(
        max_length=2,
        choices=AREAS,
        default=AREA1, 
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Detalle_Encargo(models.Model):
    producto = models.ForeignKey(
        Producto, 
        related_name='producto', 
        on_delete=models.CASCADE)
    encargo = models.ForeignKey(
        Encargo, 
        on_delete=models.CASCADE)
    cantidade = models.IntegerField()


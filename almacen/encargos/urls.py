"""
Book: Building RESTful Python Web Services
Chapter 3: Improving and adding authentication to an API with Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.conf.urls import url
from encargos import views


urlpatterns = [
    url(r'^encargos/$', 
        views.EncargoList.as_view(),
        name=views.EncargoList.name),
    url(r'^encargos/(?P<pk>[0-9]+)/$', 
        views.EncargoDetail.as_view(),
        name=views.EncargoDetail.name),
    url(r'^productos/$', 
        views.ProductoList.as_view(),
        name=views.ProductoList.name),
    url(r'^productos/(?P<pk>[0-9]+)/$', 
        views.ProductoDetail.as_view(),
        name=views.ProductoDetail.name),
    url(r'^detalle_encargo/$', 
        views.Detalle_EncargoList.as_view(),
        name=views.Detalle_EncargoList.name),
    url(r'^detalle_encargo/(?P<pk>[0-9]+)/$', 
        views.Detalle_EncargoDetail.as_view(),
        name=views.Detalle_EncargoDetail.name),
    url(r'^users/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]

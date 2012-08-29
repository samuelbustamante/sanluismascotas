from django.contrib.auth import views
from django.conf.urls.defaults import *
from myproject.zoo.views import *

urlpatterns = patterns('',
    url(r'^$', inicio),
    url(r'^ingresar/$', views.login, {'template_name': 'zoo/login.html'}),
    url(r'^registrarse/$', registrarse),
    url(r'^salir/$', views.logout, {'next_page': '/'}),

    url(r'^ver_mis_mascotas/$', mis_mascotas),
    url(r'^crear/mascota/$', crear_mascota),
    url(r'^editar/mascota/(?P<id>\d+)/$', editar_mascota),
    url(r'^borrar/mascota/(?P<id>\d+)/$', borrar_mascota),
    url(r'^mostrar/mascotas/(?P<tipo>[a-z])/$', mostrar),
    url(r'^search/$', search)
)

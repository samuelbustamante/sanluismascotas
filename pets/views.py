# -*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import create_update
from django.views.generic import list_detail
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.contrib import auth
from myproject.zoo.models import *
from myproject.zoo.forms import *

def inicio(request):
    eventos = EventoZoonosis.objects.order_by('-fecha')[0:4]
    pets = Mascota.objects.all().order_by('-id')[:4]
    pets_z = MascotaZoonosis.objects.all().order_by('-id')[:4]
    form = SearchForm()
    return render_to_response('zoo/inicio.html', locals(), context_instance=RequestContext(request))

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            especie = form.cleaned_data['especie']
            tipo = form.cleaned_data['tipo']
            mascotas = Mascota.objects.filter(especie=especie, tipo=tipo)
            if tipo == u'a':
                mascotas_z = MascotaZoonosis.objects.filter(especie=especie, adoptado=False)
            return render_to_response('zoo/search.html', locals(), context_instance=RequestContext(request))
    else:
        redirect('/')

def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            register = True
            return render_to_response('zoo/registrarse.html', locals(), context_instance=RequestContext(request))
    else:
        form = UserCreationForm()
    return render_to_response('zoo/registrarse.html', locals(), context_instance=RequestContext(request))

@login_required()
def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.usuario = request.user
            mascota.save()
            created = True
            return render_to_response('zoo/crear_mascota.html', locals(), context_instance=RequestContext(request))
    else:
        form = MascotaForm()
    return render_to_response('zoo/crear_mascota.html', locals(), context_instance=RequestContext(request))

@login_required()
def editar_mascota(request, id):
    return create_update.update_object(
        request,
        object_id = id,
        form_class = MascotaForm,
        post_save_redirect = '/ver_mis_mascotas/'
    )

@login_required()
def borrar_mascota(request, id):
    return create_update.delete_object(
        request,
        model=Mascota,
        object_id=id,
        post_delete_redirect='/ver_mis_mascotas/'
    )

@login_required()
def mis_mascotas(request):
    mascotas = Mascota.objects.filter(usuario=request.user)
    return render_to_response('zoo/ver_mascotas.html', locals(), context_instance=RequestContext(request))

def get_tipo(choices, type):
    for choice in choices:
        if choice[0] == type:
            return choice[1]

def mostrar(request, tipo):
    perros = Mascota.objects.filter(tipo=tipo, especie='p')
    gatos = Mascota.objects.filter(tipo=tipo, especie='g')
    if tipo == u'a':
        perros_z = MascotaZoonosis.objects.filter(especie='p', adoptado=False)
        gatos_z = MascotaZoonosis.objects.filter(especie='g', adoptado=False)
    tipo = get_tipo(TIPO, tipo)
    return render_to_response('zoo/mostrar.html', locals(), context_instance=RequestContext(request))

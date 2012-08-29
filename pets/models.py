# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField

TIPO = (
    ('a', u'para Adopción'),
    ('e', u'Encontradas'),
    ('p', u'Perdidas'),
)

SEXO = (
    ('m', u'macho'),
    ('h', u'hembra')
)

ESPECIE = (
    ('p', u'Perro'),
    ('g', u'Gato')
)

EDAD = (
    ('0', u'Cachorro'),
    ('1', u'1-3 años'),
    ('2', u'3-7 años'),
    ('3', u'7-10 años'),
    ('4', u'Mas de 10 años')
)

TAMANIO = (
    ('c', u'Chico'),
    ('m', u'Mediano'),
    ('g', u'Grande')
)

PELAJE = (
    ('c', u'Corto'),
    ('l', u'Largo')
)

class Mascota(models.Model):
    usuario = models.ForeignKey(User)
    nombre = models.CharField('Nombre', max_length=20)
    raza = models.CharField('Raza', max_length=50)
    tipo = models.CharField('Tipo', max_length=1, choices=TIPO)
    especie = models.CharField('Especie', max_length=1, choices=ESPECIE)
    edad = models.CharField('Edad', max_length=1, choices=EDAD)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO)
    tamanio = models.CharField('Tamaño' , max_length=1, choices=TAMANIO)
    pelaje = models.CharField('Pelaje', max_length=1, choices=PELAJE)
    color = models.CharField('Color', max_length=50)
    image = ImageWithThumbsField('Foto', upload_to='.', sizes=((150,150),), blank=True)
    mail = models.EmailField('Mail', max_length=30)
    telefono = models.CharField('Telefono', max_length=12, blank=True)
    comentario = models.TextField('Comentario', blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.nombre, self.comentario)

class EventoZoonosis(models.Model):
    fecha = models.DateField('Fecha')
    lugar = models.CharField(max_length=50)
    comentario = models.TextField('Comentario')

    def __unicode__(self):
        return u'%d/%d/%d - %s' % (self.fecha.day, self.fecha.month, self.fecha.year, self.lugar)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
	
class MascotaZoonosis(models.Model):
    nombre = models.CharField('Nombre', max_length=20)
    especie = models.CharField('Especie', max_length=1, choices=ESPECIE)
    edad = models.CharField('Edad', max_length=1, choices=EDAD)
    raza = models.CharField('Raza', max_length=50)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO)
    tamanio = models.CharField('Tamaño' , max_length=1, choices=TAMANIO)
    pelaje = models.CharField('Pelaje', max_length=1, choices=PELAJE)
    color = models.CharField('Color', max_length=50)
    image = ImageWithThumbsField('Foto', upload_to='.', sizes=((150,150),), blank=True)
    comentario = models.TextField('Comentario')
    adoptado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - %s' % (self.nombre, self.comentario)

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

class AdoptanteZoonosis(models.Model):
    mascota = models.ManyToManyField('MascotaZoonosis')
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    email = models.EmailField('E-mail')
    dni = models.IntegerField('DNI')
    domicilio = models.CharField('Domicilio', max_length=100)
    telefono = models.CharField('Telefono', max_length=20)
    ocupacion = models.CharField('Ocupacion', max_length=50)

    def __unicode__(self):
        return u'%s %s - %dni' % (self.nombre, self.apellido, self.dni)

    class Meta:
        verbose_name = 'Adoptante'
        verbose_name_plural = 'Adoptantes'

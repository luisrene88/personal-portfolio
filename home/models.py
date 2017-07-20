# -*- encoding : utf-8 -*-
from __future__ import unicode_literals
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Projecto(models.Model):
	nombre = models.CharField(max_length=150, blank=False)
	descripcion = models.TextField(max_length=1500, blank=True)
	estatus = models.BooleanField(default=True);

	class Meta:
		verbose_name = 'Projecto'
		verbose_name_plural = 'Projectos'

	def __unicode__(self):
		return unicode(self.nombre)

	def __str__(self):
		return self.nombre

class ImagenesProjectos(models.Model):
	projecto = models.ForeignKey(Projecto, on_delete=models.CASCADE, related_name = 'imagenes')
	image = ImageField(manual_crop="")
	principal = models.BooleanField(default=False)
	thumbnail = ImageSpecField(source='image',
								processors = [ResizeToFill(150,150)],
								format = 'JPEG',
								options={'quality' : 60}
								)
	
	def __str__(self):
		return self.image.name

	def __unicode__(self):
		return unicode(self.thumbnail.url)

	class Meta:
		verbose_name = 'Imagen'
		verbose_name_plural = 'Imagenes'



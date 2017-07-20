from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from ..models import (Projecto, ImagenesProjectos) 

class ProjectoForm(forms.ModelForm):
	class Meta:
		model = Projecto
		fields = '__all__'
		widgets = {
			'descripcion' : CKEditorWidget()
		}


class InlineImagenes(admin.TabularInline):
	model = ImagenesProjectos
	extra = 1

class ProjectoAdmin(admin.ModelAdmin):
	inlines = [InlineImagenes,]
	form = ProjectoForm
	
	class Meta:
		model = Projecto

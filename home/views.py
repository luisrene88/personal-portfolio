from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Projecto, ImagenesProjectos 
# Create your views here.


class PortfolioView(TemplateView):
	template_name = 'home/portfolio.html'

class IndexView(TemplateView):
	template_name = 'home/index.html'


from .serializers.projectos import ProjectoSerializer, ImagenProjectoSerielizer, ProjectoSerializerFull
from rest_framework import viewsets
from rest_framework import filters

class ProjectoViewSet(viewsets.ModelViewSet):
	queryset = Projecto.objects.filter(estatus=True)
	serializer_class = ProjectoSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('nombre', 'descripcion')

class ProjectoFullViewSet(viewsets.ModelViewSet):
	queryset = Projecto.objects.filter(estatus=True)
	serializer_class = ProjectoSerializerFull

class AboutView(TemplateView):
	template_name = 'home/about.html'
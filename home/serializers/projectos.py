from rest_framework import serializers
from ..models import Projecto, ImagenesProjectos


#auxiliar para solo mostrar una imagen de las que tenga siempre sobre la principal
class FilteredImageSerializer(serializers.ListSerializer):

	def to_representation(self, data):
		_data  = data.filter(principal=True)
		if len(_data) is 0:
			_data = data.all()[:1]
		return super(FilteredImageSerializer, self).to_representation(_data)

class ImagenProjectoSerielizer(serializers.ModelSerializer):
	thumbnail = serializers.ImageField()
	class Meta:
		list_serializer_class = FilteredImageSerializer
		model = ImagenesProjectos
		fields = ('image','thumbnail')

class ImagenProjectoSerielizerFull(serializers.ModelSerializer):
	original = serializers.ImageField(source='image')
	thumbnail = serializers.ImageField()
	class Meta:
		model = ImagenesProjectos
		fields = ('original','thumbnail')

class ProjectoSerializer(serializers.ModelSerializer):
	imagenes = ImagenProjectoSerielizer(many=True, read_only=True)
	
	class Meta:
		model = Projecto
		fields = ('id','nombre', 'imagenes',)

class ProjectoSerializerFull(serializers.ModelSerializer):
	imagenes = ImagenProjectoSerielizerFull(many=True, read_only=True)
	
	class Meta:
		model = Projecto
		fields = '__all__'
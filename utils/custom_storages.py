from django.conf import settings 
from storages.backends.s3boto import S3BotoStorage
from django.core.files.storage import get_storage_class
import copy


class MediaStorage(S3BotoStorage):
	location = settings.MEDIAFILES_LOCATION

class StaticStorage(S3BotoStorage):
	location = settings.STATICFILES_LOCATION

	def __init__(self, *args, **kwargs):
	    super(StaticStorage, self).__init__(*args, **kwargs)
	    self.local_storage = get_storage_class(
	        "compressor.storage.CompressorFileStorage")()
	
	def save(self, name, content):
		content2 = copy.copy(content)
		name = super(StaticStorage, self).save(name, content)
		self.local_storage._save(name, content2)
		return name




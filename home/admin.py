from django.contrib import admin
from admins.proyecto import ProjectoAdmin
# Register your models here.
from .models import Projecto


admin.site.register(Projecto, ProjectoAdmin)

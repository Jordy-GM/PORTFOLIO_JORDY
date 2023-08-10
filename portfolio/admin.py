from django.contrib import admin
from .models import Project


##agrega datos al panel de administrador con el modelo creado en models.py##
admin.site.register(Project)

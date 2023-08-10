from django.shortcuts import render
from .models import Project


def home(request):
    project = Project.objects.all()  # trae todos los objetos del modelo Project#
    return render(request, "home.html", {"PRDB": project})
    # retorna a la plantilla html y envia los objetos del modelo Project
    # en la variable project = #

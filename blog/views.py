from django.shortcuts import render, get_object_or_404
from .models import Posts


def post(requests):
    Post = Posts.objects.all()
    return render(requests, "posts.html", {"POSTBLOG": Post})


def publi_nume(request, id):
    public = get_object_or_404(Posts, pk=id)
    # si la publicacion no existe envia un 404##
    return render(request, "publi_nume.html", {"id": public})
    # renderiza a la plantilla publi_nume.html y envia a la plantilla
    # el id existente que no sea un 404 #

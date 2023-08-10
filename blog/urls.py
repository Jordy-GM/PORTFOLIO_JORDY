from django.urls import path
from .views import post, publi_nume

app_name = "blog"

urlpatterns = [
    path("posts/", post, name="posts"),
    path("<int:id>", publi_nume, name="publi_nume"),
]

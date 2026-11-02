from django.urls import path

from . import views

app_name = "disciplinas"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("criar/", views.criar, name="criar"),
    path("<int:pk>/", views.detalhe, name="detalhe"),
    path("<int:pk>/matricular/", views.matricular, name="matricular"),
]
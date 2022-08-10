from django.urls import path
from .views import CategoriasView, CrearCategoriasView, PruebaView, inicio

# rutas
urlpatterns=[
    path('inicio',inicio),
    path('prueba',PruebaView.as_view()),
    path('categorias',CategoriasView.as_view()),
    path('crear-categorias',CrearCategoriasView.as_view())
]
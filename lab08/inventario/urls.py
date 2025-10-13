# inventario/urls.py

from django.urls import path
from .views import (
    CategoriaListCreateView,
    CategoriaDetailView,
    ProductoListCreateView,
    ProductoDetailView,
)

urlpatterns = [
    path('categorias/', CategoriaListCreateView.as_view(), name='lista-categorias'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='detalle-categoria'),
    path('productos/', ProductoListCreateView.as_view(), name='lista-productos'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='detalle-producto'),
]
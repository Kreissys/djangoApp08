# inventario/views.py

# inventario/views.py

from rest_framework import generics, filters # <-- MODIFICA ESTA LÍNEA
import django_filters.rest_framework       # <-- AÑADE ESTA LÍNEA
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

# Vistas para el modelo Categoria
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Vistas para el modelo Producto
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['categoria'] # Mantenemos el filtro por categoría
    search_fields = ['nombre', 'descripcion'] # Añadimos búsqueda por nombre y descripción

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
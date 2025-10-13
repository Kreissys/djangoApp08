# inventario/serializers.py
from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    # Este campo es para MOSTRAR el nombre. Es de solo lectura.
    categoria = serializers.StringRelatedField(read_only=True)

    # Este campo es para RECIBIR el ID al crear/actualizar. Es de solo escritura.
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), source='categoria', write_only=True
    )

    class Meta:
        model = Producto
        # Incluimos ambos campos en la lista para que el serializer los reconozca.
        fields = ('id', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'categoria_id')
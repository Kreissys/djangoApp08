from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

# inventario/models.py
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    # --- AÑADE ESTA LÍNEA ---
    descripcion = models.TextField(blank=True, null=True) # blank=True permite que sea opcional
    stock = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
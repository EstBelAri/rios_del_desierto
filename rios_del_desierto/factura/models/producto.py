from django.db import models


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    nombre_producto = models.CharField(blank=False, null=False)
   

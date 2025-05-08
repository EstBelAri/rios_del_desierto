from django.db import models
from .producto import Producto
from .factura import Factura

class Compra(models.Model):
    id_compra = models.IntegerField(primary_key=True, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    cantidad = models.IntegerField(blank=False, null=False)
    valor = models.BigIntegerField(blank=False, null=False)
    id_producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    id_factura = models.ForeignKey(Factura, on_delete=models.RESTRICT)
   
    def get_nombre_producto(self):
        return self.id_producto.nombre_producto

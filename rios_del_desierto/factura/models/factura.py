from django.db import models
from cliente.models.cliente import Cliente
from functools import reduce

class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    identificacion = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    vendedor = models.CharField(blank=False, null=False)


    def get_valor_total(self):
        return reduce(lambda x, y: x + y, (compra.valor for compra in self.compra_set.all()), 0)
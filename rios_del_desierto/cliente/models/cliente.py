from django.db import models
from .tipo_documento import TipoDocumento
from .ciudad import Ciudad
from functools import reduce
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum

class Cliente(models.Model):
    identificacion = models.CharField(primary_key=True, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    nombre = models.CharField(blank=False, null=False)
    telefono = models.BigIntegerField(blank=False, null=False)
    correo = models.CharField(blank=False, null=False)
    id_tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.RESTRICT)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.RESTRICT)

    def get_tipo_documento(self):
        return self.id_tipo_documento.tipo_documento

    def get_ciudad(self):
        return self.id_ciudad.get_ciudad_pais()
    
    def get_ventas_mes(self):
        h_mes = timezone.now() - timedelta(days=30)
        facturas  = self.factura_set.filter(fecha_registro__gte=h_mes)
        return sum(factura.get_valor_total() for factura in facturas)
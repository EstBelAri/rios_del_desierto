from django.db import models


class TipoDocumento(models.Model):
    id_tipo_documento= models.IntegerField(primary_key=True, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    tipo_documento = models.CharField(blank=False, null=False)
   

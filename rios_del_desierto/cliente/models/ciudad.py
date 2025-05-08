from django.db import models


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    ciudad = models.CharField(blank=False, null=False)
    pais = models.CharField(blank=False, null=False)

    
    def get_ciudad_pais(self):
        return  f'{self.ciudad}, {self.pais}'
   

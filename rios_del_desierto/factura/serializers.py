from django.db.models import fields
from rest_framework import serializers
from .models.compra import Compra
from .models.factura import Factura


class CompraSerializer(serializers.ModelSerializer):
    
    nombre_producto = serializers.CharField(source= 'get_nombre_producto')

    class Meta:
        model = Compra
        fields = ('fecha_registro', 'cantidad', 'nombre_producto' ,'valor')

class FacturaSerializer(serializers.ModelSerializer):
    compras = CompraSerializer( many=True, read_only=True, source='compra_set')
    valor_total = serializers.IntegerField(source='get_valor_total')
    class Meta:
        model = Factura
        fields = ('id_factura', 'valor_total',  'fecha_registro', 'vendedor', 'compras')

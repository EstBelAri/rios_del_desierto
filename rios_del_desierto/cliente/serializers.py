from django.db.models import fields
from rest_framework import serializers
from .models.cliente import Cliente
from factura.serializers import FacturaSerializer


class ClienteSerializer(serializers.ModelSerializer):
    
    tipo_documento = serializers.CharField(source= 'get_tipo_documento')
    ciudad = serializers.CharField(source= 'get_ciudad')
    ventas_mes = serializers.CharField(source= 'get_ventas_mes')
    facturas = FacturaSerializer(many=True, read_only=True, source='factura_set')

    class Meta:
        model = Cliente
        fields = ('identificacion', 'fecha_registro', 'ventas_mes', 'nombre', 'telefono', 'correo', 'tipo_documento', 'ciudad', 'facturas')


class ClienteFidelizarSerializer(serializers.ModelSerializer):
    
    tipo_documento = serializers.CharField(source= 'get_tipo_documento')
    ciudad = serializers.CharField(source= 'get_ciudad')
    ventas_mes = serializers.CharField(source= 'get_ventas_mes')

    class Meta:
        model = Cliente
        fields = ('identificacion', 'fecha_registro', 'ventas_mes', 'nombre', 'telefono', 'correo', 'tipo_documento', 'ciudad')

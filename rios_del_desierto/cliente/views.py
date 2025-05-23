from rest_framework import serializers, viewsets, permissions, parsers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import Http404
from .models.cliente import Cliente
from .serializers import ClienteSerializer, ClienteFidelizarSerializer
import pandas as pd


class ClienteView(APIView):

    def get(self, request, identificacion, tipo):
        try:
            cliente = Cliente.objects.get(identificacion=identificacion, id_tipo_documento=tipo)
        except Cliente.DoesNotExist:
           raise Http404
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    
class ClientesFidelizar(APIView):

    def get(self, request):
        try:
            clientes = Cliente.objects.all()

            clientes_filtrados = [c for c in clientes if c.get_ventas_mes() > 5000000]
            clientes_ordenados = sorted(clientes_filtrados, key=lambda c: c.get_ventas_mes(), reverse=True)

        except Cliente.DoesNotExist:
           raise Http404
        
        serializer = ClienteFidelizarSerializer(clientes_ordenados, many=True)
        return Response(serializer.data)
    
class ClientesFidelizarCSV(APIView):

    def get(self, request):
        try:
            clientes = Cliente.objects.all()

            clientes_filtrados = [c for c in clientes if c.get_ventas_mes() > 5000000]
            clientes_ordenados = sorted(clientes_filtrados, key=lambda c: c.get_ventas_mes(), reverse=True)

            resultado = [
            {
                'identificacion': c.identificacion,
                'nombre': c.nombre,
                'correo': c.correo,
                'telefono': c.telefono,
                'ventas_mes': c.get_ventas_mes(),
                'tipo_documento': c.get_tipo_documento(),
                'ciudad':c.get_ciudad()
            }
            for c in clientes_ordenados
        ]
            
            df = pd.DataFrame(resultado)
            csv_data = df.to_csv(index=False,encoding='latin1')

        except Cliente.DoesNotExist:
           raise Http404
        
        response = HttpResponse(csv_data, content_type='text/csv; charset=latin-1')
        response['Content-Disposition'] = 'attachment; filename="clientes.csv"'
        return response
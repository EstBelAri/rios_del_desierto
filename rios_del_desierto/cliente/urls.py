from django.urls import path
from .views import ClienteView, ClientesFidelizar, ClientesFidelizarCSV

urlpatterns = [
    path('get_cliente/identificacion=<str:identificacion>', ClienteView.as_view(), name='clientes'),
    path('get_clientes_fidelizar', ClientesFidelizar.as_view(), name='clientes_fidelizar'),
    path('get_clientes_fidelizar_csv', ClientesFidelizarCSV.as_view(), name='clientes_fidelizar'),
]
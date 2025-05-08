from django.contrib import admin
from .models.producto import Producto
from .models.factura import Factura
from .models.compra import Compra


admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(Compra)

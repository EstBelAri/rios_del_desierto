from django.contrib import admin
from .models.ciudad import Ciudad
from .models.tipo_documento import TipoDocumento
from .models.cliente import Cliente


admin.site.register(Ciudad)
admin.site.register(TipoDocumento)
admin.site.register(Cliente)

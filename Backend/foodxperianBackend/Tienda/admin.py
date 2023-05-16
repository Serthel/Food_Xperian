from django.contrib import admin
from .models import TipoDocumento
from .models import DatoDomicilio
from .models import TiempoEntrega
from .models import TipoMetodoPago
from .models import TipoEstadoPago
from .models import EstadoEntrega
from .models import RegistroMensaje
from .models import Usuario
from .models import Notificacion
from .models import Pedido
from .models import Factura
from .models import EstadoPedido
from .models import TipoEstadoPedido


# Register your models here.


admin.site.register(TipoDocumento)
admin.site.register(DatoDomicilio)
admin.site.register(TiempoEntrega)
admin.site.register(TipoMetodoPago)
admin.site.register(TipoEstadoPago)
admin.site.register(EstadoEntrega)
admin.site.register(RegistroMensaje)
admin.site.register(Usuario)
admin.site.register(Notificacion)
admin.site.register(Pedido)
admin.site.register(Factura)
admin.site.register(EstadoPedido)
admin.site.register(TipoEstadoPedido)

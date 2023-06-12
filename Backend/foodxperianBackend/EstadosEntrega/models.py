from django.db import models
from django.contrib.auth.models import User
from Facturas.models import Factura
from DatosDomicilio.models import DatoDomicilio
from TiemposEntrega.models import TiempoEntrega

# Create your models here.

class EstadoEntrega(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    idFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    idDatoDomicilio = models.ForeignKey(DatoDomicilio, on_delete=models.CASCADE)
    idTiemposEntrega = models.ForeignKey(TiempoEntrega, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name ='Estado Entrega'
        verbose_name_plural ='Estados Entrega'
        db_table='EstadoEntrega'
        ordering=['id']

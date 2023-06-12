from django.db import models
from Facturas.models import Factura
from EstadosEntrega.models import EstadoEntrega

# Create your models here.

class Notificacion(models.Model):
    id = models.AutoField(primary_key=True)
    idFatura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    estadoEntrega = models.ForeignKey(EstadoEntrega, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.estadoEntrega}'

    class Meta:
        verbose_name ='Notificacion'
        verbose_name_plural ='Notificaciones'
        db_table='Notificacion'
        ordering=['id']

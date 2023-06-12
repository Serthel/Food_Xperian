from django.db import models
from Pedidos.models import Pedido
from TiposMetodosPago.models import TipoMetodoPago
from TiposEstadosPago.models import TipoEstadoPago

# Create your models here.


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    valorPedido = models.IntegerField(verbose_name='Valor Pedido',default=000)
    fechaFactura = models.DateTimeField(verbose_name='Fecha Factura')
    tipoMetodoPago = models.ForeignKey(TipoMetodoPago, on_delete=models.CASCADE)
    tipoEstadoPago = models.ForeignKey(TipoEstadoPago, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.valorPedido}'

    class Meta:
        verbose_name ='Factura'
        verbose_name_plural ='Facturas'
        db_table='Factura'
        ordering=['id']

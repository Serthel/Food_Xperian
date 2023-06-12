from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from EstadosPedidos.models import EstadoPedido
from Producto.models import Producto


# Create your models here.

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    idProducto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    FechaRegistro = models.DateTimeField(default=timezone.now)
    nombreTipoEstadoPago = models.CharField(max_length=45,verbose_name='Nombre Tipo Estado Pago',default= ' ')
    idEstadoPedido = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name ='Pedido'
        verbose_name_plural ='Pedidos'
        db_table='Pedido'
        ordering=['id']

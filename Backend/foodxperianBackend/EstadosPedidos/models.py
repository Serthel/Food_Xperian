from django.db import models


# Create your models here.


class EstadoPedido(models.Model):
    id = models.AutoField(primary_key=True)
    nombreEstadoPedido = models.CharField(max_length=45,verbose_name='Nombre Estado Pedido',default= ' ')


    def __str__(self):
        return f'{self.nombreEstadoPedido}'

    class Meta:
        verbose_name ='Estado Pedido'
        verbose_name_plural ='Estados Pedidos'
        db_table='EstadoPedido'
        ordering=['id']
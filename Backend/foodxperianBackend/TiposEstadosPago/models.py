from django.db import models

# Create your models here.

class TipoEstadoPago(models.Model):
    id = models.AutoField(primary_key=True)
    nombreTipoEstadoPago = models.CharField(max_length=45,verbose_name='Nombre Tipo Estado Pago',default= ' ')

    def __str__(self):
        return f'{self.nombreTipoEstadoPago}'

    class Meta:
        verbose_name = 'Tipo Estado Pago'
        verbose_name_plural = 'Tipos Estados Pago'
        db_table='TipoEstadoPago'
        ordering=['id']
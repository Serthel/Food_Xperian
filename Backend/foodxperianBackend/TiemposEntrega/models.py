from django.db import models

# Create your models here.

class TiempoEntrega(models.Model):
    id = models.AutoField(primary_key=True)
    cantidadTiempoEntrega = models.IntegerField(verbose_name='Cantidad Tiempo Entrega')
    descripcionTiempoEntrega = models.CharField(max_length=200,verbose_name='Descripcion Tiempo Entrega',default= ' ')


    def __str__(self):
        return f'{self.cantidadTiempoEntrega}'

    class Meta:
        verbose_name ='Tiempo Entrega'
        verbose_name_plural ='Tiempos Entrega'
        db_table='TiempoEntrega'
        ordering=['id']

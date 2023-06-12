from django.db import models

# Create your models here.

class TipoMetodoPago(models.Model):
    id = models.AutoField(primary_key=True)
    nombreTipoMetodoPago = models.CharField(max_length=45,verbose_name='Nombre Tipo Metodo Pago',default= ' ')

    def __str__(self):
        return f'{self.nombreTipoMetodoPago}'

    class Meta:
        verbose_name ='Tipo Metodo Pago'
        verbose_name_plural ='Tipos Metodos Pago'
        db_table='TipoMetodoPago'
        ordering=['id']


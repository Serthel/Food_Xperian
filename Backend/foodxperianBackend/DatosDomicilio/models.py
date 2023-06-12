from django.db import models

# Create your models here.

class DatoDomicilio(models.Model):
    id = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=45,verbose_name='Ciudad',default= ' ')
    localidad = models.CharField(max_length=45,verbose_name='Localidad',default= ' ')
    barrio = models.CharField(max_length=45,verbose_name='Barrio',default= ' ')
    direccion = models.CharField(max_length=45,verbose_name='Direccion',default= ' ')
    descripcionDomicilio = models.CharField(max_length=200,verbose_name='Descripcion Domicilio',default= ' ')

    def __str__(self):
        return f'{self.ciudad}'

    class Meta:
        verbose_name ='Dato Domicilio'
        verbose_name_plural ='Datos Domicilio'
        db_table='DatoDomicilio'
        ordering=['ciudad']

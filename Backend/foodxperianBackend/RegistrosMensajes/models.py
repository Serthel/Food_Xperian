from django.db import models

# Create your models here.

class RegistroMensaje(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=45,verbose_name='Nombres',default= ' ')
    apellidos = models.CharField(max_length=45,verbose_name='Apellidos',default= ' ')
    correo = models.EmailField(unique=True, verbose_name='Correo',default= ' ')
    celular = models.IntegerField(verbose_name='Celular')
    mensaje = models.CharField(max_length=200,verbose_name='Mensaje',default= ' ')

    def __str__(self):
        return f'{self. id}'

    class Meta:
        verbose_name ='Registro Mensaje'
        verbose_name_plural ='Registros Mensajes'
        db_table='RegistroMensajes'
        ordering=['id']

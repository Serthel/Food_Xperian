from django.db import models

# Create your models here.

class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombreTipoDocumento = models.CharField(max_length=45,verbose_name='Nombre Tipo Documento',default= ' ')

    def __str__(self):
        return f'{self.nombreTipoDocumento}'

    class Meta:
        verbose_name ='Tipo Documento'
        verbose_name_plural ='Tipos Documentos'
        db_table= 'TipoDocumento'
        ordering=['id']

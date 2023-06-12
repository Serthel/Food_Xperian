from django.db import models
from django.utils import timezone

# Create your models here.


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    precio = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Producto ({self.id}): {self.nombreProducto} {self.precio}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')
# Generated by Django 4.2.1 on 2023-06-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TiempoEntrega',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadTiempoEntrega', models.IntegerField(verbose_name='Cantidad Tiempo Entrega')),
                ('descripcionTiempoEntrega', models.CharField(default=' ', max_length=200, verbose_name='Descripcion Tiempo Entrega')),
            ],
            options={
                'verbose_name': 'Tiempo Entrega',
                'verbose_name_plural': 'Tiempos Entrega',
                'db_table': 'TiempoEntrega',
                'ordering': ['id'],
            },
        ),
    ]

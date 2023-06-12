# Generated by Django 4.2.1 on 2023-06-10 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TiposEstadosPago', '0001_initial'),
        ('TiposMetodosPago', '0001_initial'),
        ('Pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valorPedido', models.IntegerField(default=0, verbose_name='Valor Pedido')),
                ('fechaFactura', models.DateTimeField(verbose_name='Fecha Factura')),
                ('idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidos.pedido')),
                ('tipoEstadoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TiposEstadosPago.tipoestadopago')),
                ('tipoMetodoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TiposMetodosPago.tipometodopago')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'db_table': 'Factura',
                'ordering': ['id'],
            },
        ),
    ]

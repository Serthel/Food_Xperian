# Generated by Django 4.2.1 on 2023-05-15 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosDomicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDatosDomicilio', models.IntegerField()),
                ('ciudad', models.CharField(max_length=45)),
                ('localidad', models.CharField(max_length=45)),
                ('barrio', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('descripcionDomicilio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoEntrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEstadoEntrega', models.IntegerField()),
                ('nombreTipoEstadoPago', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPedido', models.IntegerField()),
                ('nombreTipoEstadoPago', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TiempoEntrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTiempoEntrega', models.IntegerField()),
                ('cantidaTiempoEntrega', models.CharField(max_length=45)),
                ('descripcionTiempoEntrega', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTipoDocumento', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEstadoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTipoEstadoPago', models.IntegerField()),
                ('nombreTipoEstadoPago', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEstadoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTipoEstadoPedido', models.IntegerField()),
                ('nombreTipoEstadoPedido', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMetodoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTipoMetodoPago', models.IntegerField()),
                ('nombreTipoMetodoPago', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.IntegerField()),
                ('nombres', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('numeroIdentificacion', models.IntegerField()),
                ('datosDomicilio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.datosdomicilio')),
                ('tipoDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.tipodocumento')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroMensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEstadoEntrega', models.IntegerField()),
                ('nombres', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
                ('celular', models.IntegerField()),
                ('mensaje', models.CharField(max_length=200)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNotificacion', models.IntegerField()),
                ('estadoEntrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.estadoentrega')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idFactura', models.IntegerField()),
                ('valorPedido', models.IntegerField()),
                ('fechaFactura', models.DateTimeField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.pedido')),
                ('tipoEstadoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.tipoestadopago')),
                ('tipoMetodoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.tipometodopago')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEstadoPedido', models.IntegerField()),
                ('nombreEstadoPedido', models.CharField(max_length=45)),
                ('estadoEntrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.estadoentrega')),
            ],
        ),
    ]

from django.db import models

# Create your models here.

class TipoDocumento(models.Model):
    idTipoDocumento = models.IntegerField(verbose_name='Identificador Tipo Documento',default= ' ')
    nombreTipoDocumento = models.CharField(max_length=45,verbose_name='Nombre Tipo Documento',default= ' ')

    def tipo_Documento(self):
            return "({})".format(self.tipo_Documento)

    def __str__(self):
        return self.tipo_Documento()

    class Meta:
        verbose_name ='Tipo Documento'
        verbose_name_plural ='Tipos Documentos'
        db_table= 'TipoDocumento'
        ordering=['idTipoDocumento']




class DatoDomicilio(models.Model):
    idDatoDomicilio = models.IntegerField(verbose_name='Identificador Nombre Domicilio',default= ' ')
    ciudad = models.CharField(max_length=45,verbose_name='Ciudad',default= ' ')
    localidad = models.CharField(max_length=45,verbose_name='Localidad',default= ' ')
    barrio = models.CharField(max_length=45,verbose_name='Barrio',default= ' ')
    direccion = models.CharField(max_length=45,verbose_name='Direccion',default= ' ')
    descripcionDomicilio = models.CharField(max_length=200,verbose_name='Descripcion Domicilio',default= ' ')

    def dato_Domicilio(self):
            return "({})".format(self.dato_Domicilio)

    def __str__(self):
        return self.dato_Domicilio()

    class Meta:
        verbose_name ='Dato Domicilio'
        verbose_name_plural ='Datos Domicilio'
        db_table='DatoDomicilio'
        ordering=['idDatoDomicilio']


class TiempoEntrega(models.Model):
    idTiempoEntrega = models.IntegerField(verbose_name='Identificador Tiempo Entrega',default= ' ')
    cantidadTiempoEntrega = models.IntegerField(verbose_name='Cantidad Tiempo Entrega',default= ' ')
    descripcionTiempoEntrega = models.CharField(max_length=200,verbose_name='Descripcion Tiempo Entrega',default= ' ')


    def tiempo_Entrega(self):
            return "({})".format(self.tiempo_Entrega)

    def __str__(self):
        return self.tiempo_Entrega()

    class Meta:
        verbose_name ='Tiempo Entrega'
        verbose_name_plural ='Tiempos Entrega'
        db_table='TiempoEntrega'
        ordering=['idTiempoEntrega']


class TipoMetodoPago(models.Model):
    idTipoMetodoPago = models.IntegerField(verbose_name='Identificador Tipo Metodo Pago',default= ' ')
    nombreTipoMetodoPago = models.CharField(max_length=45,verbose_name='Nombre Tipo Metodo Pago',default= ' ')

    def tipo_Metodo_Pago(self):
            return "({})".format(self.tipo_Metodo_Pago)

    def __str__(self):
        return self.tipo_Metodo_Pago()

    class Meta:
        verbose_name ='Tipo Metodo Pago'
        verbose_name_plural ='Tipos Metodos Pago'
        db_table='TipoMetodoPago'
        ordering=['idTipoMetodoPago']


class TipoEstadoPago(models.Model):
    idTipoEstadoPago = models.IntegerField(verbose_name='Identificador Tipo Estado Pago',default= ' ')
    nombreTipoEstadoPago = models.CharField(max_length=45,verbose_name='Nombre Tipo Estado Pago',default= ' ')

    def tipo_Estado_Pago(self):
            return "({})".format(self.tipo_Estado_Pago)

    def __str__(self):
        return self.tipo_Estado_Pago()

    class Meta:
        verbose_name = 'Tipo Estado Pago'
        verbose_name_plural = 'Tipos Estados Pago'
        db_table='TipoEstadoPago'
        ordering=['idTipoEstadoPago']



class EstadoEntrega(models.Model):
    idEstadoEntrega = models.IntegerField(verbose_name='Identificador Estado Entrega',default= ' ')
    nombreTipoEstadoPago = models.CharField(max_length=45,verbose_name='Nombre Tipo Estado Pago',default= ' ')

    def estado_Entrega(self):
            return "({})".format(self.estado_Entrega)

    def __str__(self):
        return self.estado_Entrega()

    class Meta:
        verbose_name ='Estado Entrega'
        verbose_name_plural ='Estados Entrega'
        db_table='EstadoEntrega'
        ordering=['idEstadoEntrega']



class Usuario(models.Model):
    idUsuario = models.IntegerField(verbose_name='Identificador Usuario',default= ' ')
    nombres = models.CharField(max_length=45,verbose_name='Nombres',default= ' ')
    apellidos = models.CharField(max_length=45,verbose_name='Apellidos',default= ' ')
    tipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numeroIdentificacion = models.IntegerField(verbose_name='Numero Identificacion',default= ' ')
    datosDomicilio = models.ForeignKey(DatoDomicilio, on_delete=models.CASCADE)

    def usuario(self):
            return "({})".format(self.usuario)

    def __str__(self):
        return self.usuario()

    class Meta:
        verbose_name ='Usuario'
        verbose_name_plural ='Usuarios'
        db_table='Usuario'
        ordering=['idUsuario']





class RegistroMensaje(models.Model):
    idEstadoEntrega = models.IntegerField(verbose_name='Identificador Estado Entrega',default= ' ')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=45,verbose_name='Nombres',default= ' ')
    apellidos = models.CharField(max_length=45,verbose_name='Apellidos',default= ' ')
    correo = models.EmailField(unique=True, verbose_name='Correo',default= ' ')
    celular = models.IntegerField(verbose_name='Celular')
    mensaje = models.CharField(max_length=200,verbose_name='Mensaje',default= ' ')

    def registro_Mensaje(self):
            return "({})".format(self.registro_Mensaje)

    def __str__(self):
        return self.registro_Mensaje()

    class Meta:
        verbose_name ='Registro Mensaje'
        verbose_name_plural ='Registros Mensajes'
        db_table='RegistroMensajes'
        ordering=['idEstadoEntrega']





class Notificacion(models.Model):
    idNotificacion = models.IntegerField(verbose_name='Identificador Notificacion',default= ' ')
    estadoEntrega = models.ForeignKey(EstadoEntrega, on_delete=models.CASCADE)

    def notificacion(self):
            return "({})".format(self.notificacion)

    def __str__(self):
        return self.notificacion()

    class Meta:
        verbose_name ='Notificacion'
        verbose_name_plural ='Notificaciones'
        db_table='Notificacion'
        ordering=['idNotificacion']


class Pedido(models.Model):
    idPedido = models.IntegerField(verbose_name='Identificador Pedido',default= ' ')
    nombreTipoEstadoPago = models.CharField(max_length=45,verbose_name='Nombre Tipo Estado Pago',default= ' ')

    def pedido(self):
            return "({})".format(self.pedido)

    def __str__(self):
        return self.pedido()

    class Meta:
        verbose_name ='Pedido'
        verbose_name_plural ='Pedidos'
        db_table='Pedido'
        ordering=['idPedido']


class Factura(models.Model):
    idFactura = models.IntegerField(verbose_name='Identificador Factura',default= ' ')
    valorPedido = models.IntegerField(verbose_name='Valor Pedido',default= ' ')
    fechaFactura = models.DateTimeField(verbose_name='Fecha Factura',default= ' ')
    tipoMetodoPago = models.ForeignKey(TipoMetodoPago, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    tipoEstadoPago = models.ForeignKey(TipoEstadoPago, on_delete=models.CASCADE)

    def factura(self):
            return "({})".format(self.factura)

    def __str__(self):
        return self.factura()

    class Meta:
        verbose_name ='Factura'
        verbose_name_plural ='Facturas'
        db_table='Factura'
        ordering=['idFactura']


class EstadoPedido(models.Model):
    idEstadoPedido = models.IntegerField(verbose_name='Identficador Estado Pedido',default= ' ')
    nombreEstadoPedido = models.CharField(max_length=45,verbose_name='Nombre Estado Pedido',default= ' ')
    estadoEntrega = models.ForeignKey(EstadoEntrega, on_delete=models.CASCADE)

    def estado_Pedido(self):
        return "({})".format(self.estado_Pedido)

    def __str__(self):
        return self.estado_Pedido()

    class Meta:
        verbose_name ='Estado Pedido'
        verbose_name_plural ='Estados Pedidos'
        db_table='EstadoPedido'
        ordering=['idEstadoPedido']


class TipoEstadoPedido(models.Model):
    idTipoEstadoPedido = models.IntegerField(verbose_name='Identificador Tipo Estado Pedido',default= ' ')
    nombreTipoEstadoPedido = models.CharField(max_length=45,verbose_name='Nombre Tipo Estado Pedido',default= ' ')

    def tipo_Estado_Pedido(self):
            return "({})".format(self.tipo_Estado_Pedido)

    def __str__(self):
        return self.tipo_Estado_Pedido()

    class Meta:
        verbose_name ='Tipo Estado Pedido'
        verbose_name_plural ='Tipos Estados Pedido'
        db_table='TipoEstadoPedido'
        ordering=['idTipoEstadoPedido']


// Realizar la solicitud GET a la API REST
axios.get('http://localhost:4200/Pedidos/getPedido')
  .then(function(response) {
    // Obtener los datos de la respuesta
    var datos = response.data;

    // Obtener la referencia a la tabla en HTML
    var tabla = document.getElementById('Tabla_Datos');
    var tbody = tabla.getElementsByTagName('tbody')[0];

    // Recorrer los datos y generar las filas de la tabla
    datos.forEach(function(dato) {
      var fila = document.createElement('tr');
      var id = document.createElement('td');
      var Cantidad = document.createElement('td');
      var FechaRegistro = document.createElement('td');
      var NombreEstadoPago = document.createElement('td');
      var Id_user = document.createElement('td');
      var Id_Producto = document.createElement('td');
      var Id_Estado_Producto = document.createElement('td');

      id.textContent = dato.id;
      Cantidad.textContent = dato.cantidad;
      FechaRegistro.textContent = dato.FechaRegistro;
      NombreEstadoPago.textContent = dato.nombreTipoEstadoPago;
      Id_user.textContent = dato.id_user;
      Id_Producto.textContent = dato.idProducto;
      Id_Estado_Producto.textContent = dato.idEstadoPedido;

      fila.appendChild(id);
      fila.appendChild(Cantidad);
      fila.appendChild(FechaRegistro);
      fila.appendChild(NombreEstadoPago);
      fila.appendChild(Id_user);
      fila.appendChild(Id_Producto);
      fila.appendChild(Id_Estado_Producto);

      tbody.appendChild(fila);
    });
  })
  .catch(function(error) {
    console.error('Error al obtener los datos:', error);
  });

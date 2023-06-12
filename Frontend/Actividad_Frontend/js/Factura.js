// Realizar la solicitud GET a la API REST
axios.get('http://127.0.0.1:4200/Facturas/getFactura')
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
      var ValorPedido = document.createElement('td');
      var FechaFactura = document.createElement('td');
      var idPedido = document.createElement('td');
      var MetodoPago = document.createElement('td');
      var EstadoPago = document.createElement('td');

      id.textContent = dato.id;
      ValorPedido.textContent = dato.valorPedido;
      FechaFactura.textContent = dato.fechaFactura;
      idPedido.textContent = dato.idPedido;
      MetodoPago.textContent = dato.tipoMetodoPago;
      EstadoPago.textContent = dato.tipoEstadoPago;

      fila.appendChild(id);
      fila.appendChild(ValorPedido);
      fila.appendChild(FechaFactura);
      fila.appendChild(idPedido);
      fila.appendChild(MetodoPago);
      fila.appendChild(EstadoPago);

      tbody.appendChild(fila);
    });
  })
  .catch(function(error) {
    console.error('Error al obtener los datos:', error);
  });

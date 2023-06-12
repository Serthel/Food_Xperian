// Importar Axios desde un módulo externo o incluirlo en tu proyecto

// Realizar la solicitud GET a la API REST
axios.get('http://127.0.0.1:4200/EstadosEntrega/getEstadoEntrega')
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
      var IdUsuario = document.createElement('td');
      var IdFactura = document.createElement('td');
      var IdDomicilio = document.createElement('td');
      var IdTiempoEntrega = document.createElement('td');

      id.textContent = dato.id;
      IdUsuario.textContent = dato.id_user;
      IdFactura.textContent = dato.idFactura;
      IdDomicilio.textContent = dato.idDatoDomicilio;
      IdTiempoEntrega .textContent = dato.idTiemposEntrega;

      fila.appendChild(id);
      fila.appendChild(IdUsuario);
      fila.appendChild(IdFactura);
      fila.appendChild(IdDomicilio);
      fila.appendChild(IdTiempoEntrega);

      tbody.appendChild(fila);
    });
  })
  .catch(function(error) {
    console.error('Error al obtener los datos:', error);
  });
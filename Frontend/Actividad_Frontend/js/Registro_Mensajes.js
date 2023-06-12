// Importar Axios desde un módulo externo o incluirlo en tu proyecto

// Realizar la solicitud GET a la API REST
axios.get('http://127.0.0.1:4200/RegistrosMensajes/getRegistroMensaje')
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
      var Nombres = document.createElement('td');
      var Apellidos = document.createElement('td');
      var Correo = document.createElement('td');
      var Celular = document.createElement('td');
      var Mensaje = document.createElement('td');

      id.textContent = dato.id;
      Nombres.textContent = dato.nombres;
      Apellidos.textContent = dato.apellidos;
      Correo.textContent = dato.correo;
      Celular.textContent = dato.celular;
      Mensaje.textContent = dato.mensaje;

      fila.appendChild(id);
      fila.appendChild(Nombres);
      fila.appendChild(Apellidos);
      fila.appendChild(Correo);
      fila.appendChild(Celular);
      fila.appendChild(Mensaje);

      tbody.appendChild(fila);
    });
  })
  .catch(function(error) {
    console.error('Error al obtener los datos:', error);
  });
// Realizar la solicitud GET a la API REST
axios.get('http://127.0.0.1:4200/DatosDomicilio/getDatoDomicilio')
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
      var Ciudad = document.createElement('td');
      var Localidad = document.createElement('td');
      var Barrio = document.createElement('td');
      var Direccion = document.createElement('td');
      var Descripcion_Domicilio = document.createElement('td');

      id.textContent = dato.id;
      Ciudad.textContent = dato.ciudad;
      Localidad.textContent = dato.localidad;
      Barrio.textContent = dato.barrio;
      Direccion.textContent = dato.direccion;
      Descripcion_Domicilio.textContent = dato.descripcionDomicilio;

      fila.appendChild(id);
      fila.appendChild(Ciudad);
      fila.appendChild(Localidad);
      fila.appendChild(Barrio);
      fila.appendChild(Direccion);
      fila.appendChild(Descripcion_Domicilio);

      tbody.appendChild(fila);
    });
  })
  .catch(function(error) {
    console.error('Error al obtener los datos:', error);
  });

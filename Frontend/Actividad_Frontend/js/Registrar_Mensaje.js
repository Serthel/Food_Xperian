document.getElementById('Registrar_Mensaje').addEventListener('submit', function(event) {
    event.preventDefault();

    // Obtener los valores de los campos del formulario
    var nombres = document.getElementById('nombres').value;
    var apellidos = document.getElementById('apellidos').value;
    var correo = document.getElementById('correo').value;
    var celular = document.getElementById('celular').value;
    var mensaje = document.getElementById('mensaje').value;

    // Crear un objeto con los datos del mensaje
    var mensajeData = {
      nombres: nombres,
      apellidos: apellidos,
      correo: correo,
      celular: celular,
      mensaje: mensaje
    };

    // Convertir el objeto a formato JSON
    var jsonData = JSON.stringify(mensajeData);

    // Realizar la petición POST utilizando Axios
    axios.post('http://127.0.0.1:4200/RegistrosMensajes/createRegistroMensaje', jsonData, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(function(response) {
        // La petición se ha realizado con éxito
        console.log(response.data); // Puedes hacer algo con la respuesta del servidor

        // Mostrar mensaje de SweetAlert2
        Swal.fire({
          icon: 'success',
          title: 'Mensaje enviado',
          text: 'Tu mensaje ha sido enviado correctamente.'
        }).then(function() {
          // Limpiar los datos del formulario
          document.getElementById('Registrar_Mensaje').reset();
        });
      })
      .catch(function(error) {
        // Ocurrió un error en la petición
        console.error(error);

        // Mostrar mensaje de SweetAlert2
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'No se pudo enviar el mensaje.'
        }).then(function() {
          // Limpiar los datos del formulario
          document.getElementById('Registrar_Mensaje').reset();
        });
      });
  });

document.getElementById('Registrar_usuario').addEventListener('submit', function (event) {
  event.preventDefault();

  // Obtener los valores de los campos del formulario
  var usuario = document.getElementById('usuario').value;
  var correo = document.getElementById('correo').value;
  var contraseña_1 = document.getElementById('contraseña_1').value;
  var contraseña_2 = document.getElementById('contraseña_2').value;

  // Crear un objeto con los datos del usuario
  var usuarioData = {
    username: usuario,
    email: correo,
    password1: contraseña_1,
    password2: contraseña_2
  };

  // Convertir el objeto a formato JSON
  var jsonData = JSON.stringify(usuarioData);

  // Realizar la petición POST utilizando Axios
  axios.post('http://127.0.0.1:4200/auth/registration/', jsonData, {
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(function (response) {
      // La petición se ha realizado con éxito
      console.log(response.data); // Puedes hacer algo con la respuesta del servidor

      // Mostrar mensaje de SweetAlert2
      Swal.fire({
        icon: 'success',
        title: 'Exito',
        text: 'Usuario registrado exitosamente'
      }).then(function () {
        // Limpiar los datos del formulario
        document.getElementById('Registrar_usuario').reset();

        window.location.href = 'http://localhost:3000/';
      });
    })
    .catch(function (error) {
      // Ocurrió un error en la petición
      console.error(error);

      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Error al registrar usuario.'
      }).then(function () {
        // Limpiar los datos del formulario
        document.getElementById('Registrar_usuario').reset();
      });
    });
});


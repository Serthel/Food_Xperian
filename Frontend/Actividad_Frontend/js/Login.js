function handleLogin(event) {
  event.preventDefault();

  // Obtener los valores del formulario
  var usuario = document.getElementById('usuario').value;
  var correo = document.getElementById('correo').value;
  var contraseña = document.getElementById('contraseña').value;

  // Crear un objeto con los datos del usuario
  var userData = {
    username: usuario,
    email: correo,
    password: contraseña
  };

  // Enviar los datos al servidor en formato JSON utilizando Axios
  axios.post('http://127.0.0.1:4200/dj-rest-auth/login/', JSON.stringify(userData), {
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(function (response) {
      // Manejar la respuesta del servidor
      var token = response.data.token;
      // Guardar el token en el almacenamiento local (localStorage)
      localStorage.setItem('token', token);

      Swal.fire({
        icon: 'success',
        title: 'Autenticacion Exitosa',
        text: 'Tu mensaje ha sido enviado correctamente.',
        showConfirmButton: false,
        timer: 15000
      }).then(function () {
        // Limpiar los datos del formulario
        document.getElementById('loginForm').reset();
      });

      // Redireccionar a otra página si el inicio de sesión es exitoso
      window.location.href = 'http://localhost:3000/html/home.html';
    })
    .catch(function (error) {
      // Manejar los errores de la petición
      console.error(error);

      // Mostrar mensaje de SweetAlert2
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'error en proceso de autenticacion.',
        showConfirmButton: false,
        timer: 15000
      });
    }).then(function () {
      // Limpiar los datos del formulario
      document.getElementById('loginForm').reset();
    });
}

document.getElementById('loginForm').addEventListener('submit', handleLogin);

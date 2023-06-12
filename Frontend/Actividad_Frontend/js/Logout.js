
const axios = require('axios');

// Función para cerrar sesión
function logout() {
  // Eliminar el token del almacenamiento local (localStorage)
  localStorage.removeItem('token');

  Swal.fire({
    icon: 'success',
    title: 'Logout',
    text: 'Cierre de sesion exitoso.',
    showConfirmButton: false,
    timer: 15000
  })
  // Redireccionar al archivo "index.html"
  window.location.href = 'http://localhost:3000/';
}
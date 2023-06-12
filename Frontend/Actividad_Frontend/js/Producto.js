// Función para generar las cards con los datos recibidos
function generateCards(data) {
    var cardsContainer = document.getElementById('cardsContainer');

    data.forEach(function(item) {
      var card = document.createElement('div');
      card.classList.add('col-md-4');

      var image = document.createElement('img');
      image.src = item.imagen;

      var cardBody = document.createElement('div');
      cardBody.classList.add('card-body');

      var title = document.createElement('h6');
      title.classList.add('card-title');
      title.textContent = item.nombreProducto;

      var description = document.createElement('p');
      description.classList.add('card-text');
      description.textContent = item.descripcion;

      var price = document.createElement('p');
      price.classList.add('card-text');
      price.textContent = 'Precio: ' + item.precio;

      cardBody.appendChild(title);
      cardBody.appendChild(description);
      cardBody.appendChild(price);
      card.appendChild(image);
      card.appendChild(cardBody);

      cardsContainer.appendChild(card);
    });
  }

  // Obtener los datos del API REST utilizando Axios
  axios.get('http://127.0.0.1:4200/Producto/getProducto')
    .then(function(response) {
      var data = response.data;
      generateCards(data);
    })
    .catch(function(error) {
      console.error(error);
    });
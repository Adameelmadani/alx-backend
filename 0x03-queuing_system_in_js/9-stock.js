var listProducts = [{Id: 1, name: Suitcase 250, price: 50, stock: 4},
  {Id: 2, name: Suitcase 450, price: 100, stock: 10},
  {Id: 3, name: Suitcase 650, price: 350, stock: 2},
  {Id: 4, name: Suitcase 1050, price: 550, stock: 5}
];

function getItemById(id) {
  for (var i = 0; i < listProducts.length; i++) {
    if (listProducts[i].Id === id)
      return listProducts[i];
  }
}

const express = require('express');
const app = express();
const PORT = 1245;

app.get('/list_products', (req, res) => {
  var json_list = [{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},{"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},{"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},{"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}];
  res.json(json_list);
});

app.listen(PORT, () => {
});

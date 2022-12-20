function pizzaOven(crustType, sauceType, cheeses, toppings) {
  var pizza = {};
  pizza.crustType = crustType;
  pizza.sauceType = sauceType;
  pizza.cheeses = cheeses;
  pizza.toppings = toppings;
  return pizza;
}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
// console.log(pizza1);

var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
// console.log(pizza2);

var pizza3 = pizzaOven("thin crust", "buffalo", ["mozzarella"], ["chicken", "red onions", "green onions"]);
// console.log(pizza3);

var pizza4 = pizzaOven("stuffed crust", "white garlic", ['provolone'], ["pepperoni", "green peppers", "black olives", "sausage"]);
// console.log(pizza4);

function randomPizza() {
  var pizza = {
    "crustType": ["deep dish", "hand tossed", "thin crust", "stuffed crust"],
    "sauceType": ["traditional", "marinara", "buffalo", "white garlic"],
    "cheeses": ["mozzarella", "feta", "provolone", "cheddar"],
    "toppings": [["pepperoni", "sausage"], ["mushrooms", "olives"], ["chicken", "onions"], ["green peppers", "red onions"]]
  }
  var randomPizza = [];

  function randomNumber() {
    return Math.floor(Math.random() * 4);
  }

  randomPizza.push(pizza.crustType[randomNumber()]);
  randomPizza.push(pizza.sauceType[randomNumber()]);
  randomPizza.push(pizza.cheeses[randomNumber()]);
  randomPizza.push(pizza.toppings[randomNumber()]);

  return randomPizza;
}

console.log(randomPizza());
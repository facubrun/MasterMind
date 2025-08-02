var suma = 2 + '2'; //'22' js pasa todo a str

// Los tipos de javascript:
var numero = 2;

var string = 'text';

var booleano = true;

var array = ["aa", "bb", 3, [1, 2]]; //indexed

var objeto = { // keys
    nombre: 'name', 
    apellido: '0',
    edad: 120
}

var nombreFuncion = function() {}
// null y undefined
// null NO tiene definido un valor
var valorNulo = null;
var valorUndefined;
console.log(typeof valorNulo, typeof valorUndefined);

valorUndefined = 5;
// los tipos son dinamicos -> cambian valor y tipo sin problemas

// typeof -> para saber de que tipo es una variable
console.log(typeof booleano == 'string')


//vectores
var vector = [];
vector.push(3);
vector.push(4);
vector.pop();

console.log(vector);

//objetos
var objeto = {nombre: 'name'};
objeto[apellido] = 'none';










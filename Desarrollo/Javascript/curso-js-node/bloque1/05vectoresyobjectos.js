var array = ["aa", "bb", 3, [1, 2], {nombre: 'Nombre', apellido: 'Apellido'}];
var objeto = {
    nombre: 'name', 
    apellido: 'none',
    edad: 120,
    libros: ['DUNE', 'Simbolos'],
    direccion: {
        calle: 'psje 88',
        numero: 4
    }
}

var item0 = array[0];
var item1 = array[1];

var indice = 4;
var item4 = array[indice].nombre;

var objetoNombre = objeto.nombre;
var calle = objeto.direccion.calle;


var item50 = array[50];
console.log(item50); // item 50 no existe pero js no se rompe

var piso = objeto.piso[1]; // property piso no existe pero js no se rompe
console.log(piso);

var longitud = array.length

var isValidPosition = 50 >= 0 && 50 < array.length
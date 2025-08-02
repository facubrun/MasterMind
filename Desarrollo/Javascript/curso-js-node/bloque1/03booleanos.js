var booleanoCierto = true;
var booleanoFalso = false;

var a = '10';
var b = 10;

var aMayorQueb = a > b;
// > < >= <= == === != !==

console.log(a === b); // compara tanto valor como tipo, si alguno es distinto da false!

var inicio = 0;
var final = 100;
var numero = 101;

var mayorQueInicio = numero > inicio;
var menorQueFinal = numero < final;
var dentroDeRango = mayorQueInicio && menorQueFinal;
console.log(dentroDeRango);
/* AND (&&) Tabla de verdad
1 && 1 : 1
1 && 0 : 0
0 && 1 : 0
0 && 0 : 0
*/

/* OR (||) Tabla de verdad
1 || 1 : 1
1 || 0 : 1
0 || 1 : 1
0 || 0 : 0
*/

/* NOT (!) Tabla de verdad
1 : 0
0 : 1
*/

var TrabajoHecho = true;
var notaExamenFinal = 10;
var FaltaTecnica = true;
var CursoAprobado = (TrabajoHecho || notaExamenFinal >= 5) && !FaltaTecnica;
console.log(CursoAprobado);
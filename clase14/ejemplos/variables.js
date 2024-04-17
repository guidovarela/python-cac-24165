/*
var se utiliza para declarar una variable llamada variableVar. Con var, puedes redeclarar y actualizar la variable sin problemas. Sin embargo, se considera una práctica obsoleta y puede conducir a problemas de alcance (scope).

let se usa para declarar una variable llamada variableLet. A diferencia de var, no puedes redeclarar una variable let en el mismo ámbito, pero puedes actualizar su valor.

const se usa para declarar una variable llamada variableConst. Las variables const son constantes y no se pueden redeclarar ni actualizar una vez que se les ha asignado un valor.
*/

// Declaración con var
var variableVar = "Soy una variable con var";
var variableVar = "Puedo ser redeclarada con var";
variableVar = "Puedo ser actualizada con var";

// Declaración con let
let variableLet = "Soy una variable con let";
variableLet = "Puedo ser actualizada con let";

// Declaración con const
const variableConst = "Soy una variable constante";
// No se puede redeclarar ni actualizar una constante
// variableConst = "Esto dará error";

console.log(variableVar); // Imprime "Puedo ser actualizada con var"
console.log(variableLet); // Imprime "Puedo ser actualizada con let"
console.log(variableConst); // Imprime "Soy una variable constante"
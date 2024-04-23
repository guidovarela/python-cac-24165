/*Bucle WHILE*/

// i = 0; // Inicialización de la variable contador
// // Condición: Mientras la variable contador sea menor de 5
// while (i < 5) {
//   console.log("Valor de i:", i);
//   i = i + 1; // Incrementamos el valor de i (Alternativa: i++)
// }

//Otro ejemplo: Leer notas hasta que ingrese -1
let nota=0;
// nota=Number(prompt("Ingrese una nota (para finalizar ingrese -1):"));

while (nota != -1 && nota == true){//mientras la nota no sea -1
  nota=Number(prompt("Ingrese una nota (para finalizar ingrese -1):" ));

  document.write(nota + "<br>")
}


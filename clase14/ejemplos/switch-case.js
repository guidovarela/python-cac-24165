/*
El uso de switch...case es útil cuando necesitas tomar decisiones basadas en un valor específico y quieres tener múltiples casos posibles con diferentes acciones.

Tenemos una variable llamada diaDeLaSemana que representa un día de la semana (en este caso, 3, que corresponde al miércoles).
Utilizamos la estructura switch para evaluar el valor de diaDeLaSemana.
Dentro de cada case, especificamos un valor posible de diaDeLaSemana y asignamos el nombre correspondiente del día a la variable nombreDelDia.
El bloque default se ejecutará si diaDeLaSemana no coincide con ninguno de los case anteriores. En este caso, asignamos "Día no válido" a nombreDelDia.
Finalmente, imprimimos el nombre del día en la consola.
En este ejemplo, el resultado será "Hoy es Miércoles" porque diaDeLaSemana es igual a 3. 
*/

let diaDeLaSemana = 1;
let nombreDelDia;

/*if(diaDeLaSemana == 6){
    nombreDelDia = "Lunes";
}*/

switch (diaDeLaSemana) {
    case 1:
        nombreDelDia = "Lunes";
        break;
    case 2:
        nombreDelDia = "Martes";
        break;
    case 3:
        nombreDelDia = "Miércoles";
        break;
    case 4:
        nombreDelDia = "Jueves";
        break;
    case 5:
        nombreDelDia = "Viernes";
        break;
    case 6:
        nombreDelDia = "Sábado";
        break;
    case 7:
        nombreDelDia = "Domingo";
        break;
    default:
        nombreDelDia = "Día no válido";
}

console.log("Hoy es " + nombreDelDia);

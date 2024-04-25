/************** ARRAYS *****************/
const array = ["a", "b", "c"];

// console.log(array[0]); // 'a'
// console.log(array[2]); // 'c'
// console.log(array[5]); // undefined
// console.log(array.length); // 3

/*-----------------------------------*/
const vector= [1,3,5,8]; //0, 1, 2, 3: cantidad de elementos - 1
const vectorVacio= []; //Vector vacío
const vectorDos = new Array("a", "b", "c");
const vectorTres = new Array (1, 5, 10, 15, 20);

var frutas = ["Banana", "Naranja", "Manzana", "Mango"];

/* .push(obj1, obj2...): Añade uno o varios elementos al final del array. Devuelve tamaño del array.*/

// document.write("PUSH <br>");
// document.write(frutas, "<br>");
// frutas.push("Kiwi", "Pera");
// document.write(frutas);

/* .pop(): Elimina y devuelve el último elemento del array.*/

// document.write("<br><br>POP <br>");
// document.write(frutas, "<br>");
// var frutaEliminada = frutas.pop(); //No tiene argumentos
// document.write(frutas);
// document.write("<br> Fruta eliminada: ", frutaEliminada);

/*.unshift(obj1, obj2...): Añade uno o varios elementos al inicio del array. Devuelve tamaño del array.*/

// var colores = ["Rojo", "Amarillo", "Verde", "Celeste"];
// document.write("<br><br> UNSHIFT <br>");
// document.write(colores, "<br>");
// colores.unshift("Azul", "Naranja");
// document.write(colores);

/*.shift(): Elimina y devuelve el primer elemento del array.*/

// document.write("<br><br> SHIFT <br>");
// document.write(colores, "<br>");
// var colorEliminado = colores.shift(); //No tiene argumentos
// document.write(colores);
// document.write("<br> Color eliminado: ", colorEliminado);

/************** Objetos *****************/
/*Creación de Objetos:
Puedes crear objetos en JavaScript de varias maneras. La forma más común es utilizando la sintaxis de llaves {} para definir un objeto literal.
*/
const persona = {
    nombre: "Juan",
    edad: 30,
    ciudad: "Ejemploville",
    decirHola: function() {
        console.log("¡Hola!");
    }
};

let libros = [
    {
        titulo: "El Gran Gatsby",
        autor: "F. Scott Fitzgerald",
        añoPublicacion: 1925
    },
    {
        titulo: "Cien años de soledad",
        autor: "Gabriel García Márquez",
        añoPublicacion: 1967
    },
    {
        titulo: "1984",
        autor: "George Orwell",
        añoPublicacion: 1949
    }
];

/*Puedes acceder a las propiedades de un objeto utilizando la notación de punto (objeto.propiedad) o la notación de corchetes (objeto['propiedad']). Por ejemplo:
*/
console.log(persona.nombre); // Accede al valor de la propiedad nombre
console.log(persona['edad']); // Accede al valor de la propiedad edad


/*
Modificación de Propiedades:
Puedes modificar el valor de una propiedad de un objeto de esta manera:
*/
persona.edad = 31; 

/*Agregar Nuevas Propiedades:
Puedes agregar nuevas propiedades a un objeto en cualquier momento:
*/
persona.email = "juan@example.com"; 


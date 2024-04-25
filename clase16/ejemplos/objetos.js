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


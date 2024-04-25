
const persona = {
    nombre: "Juan",
    edad: 30,
    ciudad: "Ejemploville",
    decirHola: function() {
        console.log("¡Hola!");
    }
};

/*Iteración sobre Propiedades:
Puedes recorrer las propiedades de un objeto utilizando bucles for...in. Esto es útil cuando tienes objetos con muchas propiedades y quieres realizar operaciones en cada una de ellas.
*/
for (let propiedad in persona) {
    console.log(propiedad + ': ' + persona[propiedad]);
}
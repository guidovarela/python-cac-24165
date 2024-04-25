//Ejemplo común, sin uso de Template Strings
function ejemplo(){
    var temp= `Hola, mi nombre es Pablo`;
    console.log(temp);
}

//Ejemplo usando Template Strings
function ejemploDos(nombre, edad){
    //console.log("Mi nombre es " + nombre + " y mi edad es " + edad);
    console.log(`Mi nombre es ${nombre} y mi edad es ${edad}`);
}
ejemplo();
ejemploDos("Carlos", 32);
// var nom = prompt("Introduce tu nombre");
// var ed = prompt("Introduce tu edad");
// ejemploDos(nom, ed);

var cadena = `Línea número 1 
Línea número 2`;
console.log(cadena);

var saludo = "Hola Mundo!"
var saludo = "otro dato"

//ES6 
// let / const

let saludo1 = "otra vez, Hola Mundo!"
saludo1 = "otro dato"

//console.log(saludo1)

//Palabras reservadas
// var let if function const ...
//let var = "esto es una variable";

const pi = 3.141593 
//pi = "otro dato" 
//console.log(pi)


//Estructuras condicionales -> if/else
/*
if(condicion){
    instrucciones si es verdadera
}else{
    si es falsa
}

else if
if(condicion){
    instrucciones si es verdadera
}else if(condicion2){
    si es falsa
}

*/

let edadUsuario = parseInt(prompt("Cual es tu edad?"))
let mayoriaEdad = 18

if(edadUsuario >= mayoriaEdad){
    document.write("Sos mayor de edad")
}else{
    document.write("Ups, Sos menor de edad")
}

let activado = false
let nombreUsuario = prompt("nombre de usuario...")

if(activado == true || nombreUsuario=="Jorge" && nombreUsuario != null){
    console.log("Abriendo puerta...")
}else{
    if(nombreUsuario!="Jorge"){
        console.log("Error de usuario")
    }else{
        console.log("Esperando activacion...") 
    }
}

//-------------------

let nota = 6

if(nota >= 0 && nota <= 3){
    console.log("Desaprobado")
    }else if(nota >= 4 && nota < 6){
        console.log("Suficiente")
        }else if(nota >=6 && nota <=8){
            console.log("Bueno")
            }else{
                console.log("Muy Bueno")
                }
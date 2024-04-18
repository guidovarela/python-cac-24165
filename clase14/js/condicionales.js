// Condicionales
// if / 

/*
 if(condicion){
    //verdadero

}else{
    //condicion falsa
}

*/

let edadUsuario = parseInt(prompt("Inserte su edad"))
let mayoriaEdad = 18
let esUsuario = true

// if(esUsuario == true && edadUsuario >= mayoriaEdad){
//     // console.log("El usuario es mayor de edad")
//     console.log("Bienvenido!")
// }else{
//     // console.log("El usuario es menor de edad")
//     console.log("Acceso denegado")
// }

let comprobacion = edadUsuario>=mayoriaEdad && esUsuario ? "Bienvenido!" : "Acceso denegado"
document.write(comprobacion)

// let nota = parseInt(prompt("Insertar la nota: "))
// aprobado >= 4
// bien >= 6
// muy bien = 8
// excelente >= 9


// if (nota >= 4 && nota <6) {
//     console.log("aprobado")
//     } else if(nota >= 6 && nota <8) {
//         console.log("bien")    
//         } else if(nota >= 8 && nota <9 ) {
//             console.log("Muy bien")    
//             }else if(nota >= 9 && nota <=10) {
//                 console.log("excelente")   
//             }else if(nota > 10){
//                 console.log("Dato erroneo!")
//             }else{
//             console.log("desaprobado") 
//             }

// comparaciones
// = asignacion
// == comparacion valor
// === comparacion valor + tipo de dato

let data = 10

if(data === 10){
    document.write("dato correcto")
}else{
    document.write("dato falso")
}
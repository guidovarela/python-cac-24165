
// let animal1 = "perro"
// let animal2 = "gato"
// let animal3 = "elefante"
// let animal4 = "cocodrilo"

// array / vector / arreglo / matriz

//let animales = new Array()
let animales = []

// document.write(animales.length)

// array.push()
// array.unshift()
// shift()
// pop()
// sort()

function agregarDato(arreglo,dato){
    arreglo.push(dato)
    // arreglo.unshift(dato)
}
function eliminarDato(arreglo){
    // arreglo.pop()
    // arreglo.splice(pos,cant)
    arreglo.shift()
}
// buscar indice
// let indice = animales.indexOf("Leon"); 

eliminarDato(animales)

// agregarDato(animales,prompt("Inserte el animal"))
agregarDato(animales,"leon")
agregarDato(animales,"Cabra")
agregarDato(animales,"camello")


//Recorremos el array
for (let i = 0; i < animales.length; i++) {
    document.write("<p style='border:solid;padding:10px'>"+animales[i]+"</p>")
    console.log(animales[i])
}


let provincias = [
    "Buenos Aires",   "Córdoba",   "Santa Fe",   "Ciudad Autónoma de Buenos Aires",   "Mendoza",   "Tucumán",   "Entre Ríos",   "Salta",   "Misiones",   "Chaco",   "Corrientes" , "Santiago del Estero",    "San Juan",    "Jujuy",    "Río Negro",    "Neuquén",    "Formosa",    "Chubut",    "San Luis",    "Catamarca",    "La Rioja",    "La Pampa",    "Santa Cruz",    "Tierra del Fuego, Antártida e Islas del Atlántico Sur"   ];

    //for of / for in
    // for (data of provincias) {

    //     document.write("<option>"+data+"</option>")
        
    //     //console.log(data)
    // }

    for (data in provincias) {
        document.write("<option>"+data+"</option>")

        //provincias[data]
    }



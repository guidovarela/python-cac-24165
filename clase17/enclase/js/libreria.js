
//Definimos la Clase Libro
class Libro {
    constructor(tit,aut,lan,sto){
        this.titulo=tit
        this.autor=aut
        this.lanzamiento=lan
        this.stock=sto
    }

}

let libros =[] 

function cargarLibros(){
    let contenedorLibros = document.querySelector("#libros-oferta")
    //vaciar el contenedor
    contenedorLibros.innerHTML=""
    for (const iterator of libros) {
        contenedorLibros.innerHTML+=iterator.titulo+" "+iterator.autor+" "+iterator.lanzamiento+"<br>"
    }
}

//crear una funcion para crear el objeto
function crearLibro(e){
    //aulamos la accion de submit del form (HTML)
    e.preventDefault()
    
    //to-do: definir validacion de datos
    let tit_l = document.getElementById("titulo").value
    let aut_l = document.getElementById("autor").value
    let lan_l = document.getElementById("lanzamiento").value
    let sto_l = document.getElementById("stock").value

    //instancia -> nuevo objeto
    let nuevoLibro = new Libro(tit_l,aut_l,lan_l,sto_l)

    libros.push(nuevoLibro)

    cargarLibros()

    formCargaLibros.reset()

    //almacernarlo en Web Storage
    localStorage.setItem("tit_1",tit_l)
    localStorage.setItem("aut_1",aut_l)
    //otra forma:
    localStorage.lan_1=lan_l
    localStorage.sto_1=sto_l
}

function leerStorage(){
    console.log(localStorage.getItem("tit_1",tit_l))
    console.log(localStorage.getItem("aut_1",aut_l))
    console.log(localStorage.getItem("lan_1",lan_l))
    console.log(localStorage.getItem("sto_1",sto_l))
}

//ubicamos el form
let formCargaLibros = document.getElementById("form-cargar")

//addEventListener("evento",funcionAEjecutar)
formCargaLibros.addEventListener("submit",crearLibro)



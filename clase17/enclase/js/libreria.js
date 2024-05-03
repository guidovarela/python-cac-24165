//Crear la clase libros
class Libros {
    constructor(id,tit,aut,lan,sto){
        this.id=id
        this.titulo=tit,
        this.autor=aut,
        this.lanzamiento=lan,
        this.stock=sto
    }
}

//Datos de acceso global
const libros = []
const formCarga = document.getElementById("form-cargar")
let contenedor = document.querySelector("#libros-oferta")

//DOM - Document Object Model
// document.getElementById()
// document.getElementsByClassName()
// document.getElementsByName()
// document.getElementsByTagName()

function cargarLibro(e){
    //cancelamos el evento por default
    e.preventDefault()
    //leer datos del form
    let campoTit = document.getElementById("titulo").value
    let campoAut = document.getElementById("autor").value
    let campoLan = document.getElementById("lanzamiento").value
    let campoSto = document.getElementById("stock").value
    let id = libros.length + 1
    //crear objeto
    const nuevoLibro = new Libros(id,campoTit,campoAut,campoLan,campoSto)
    
    //push en el array
    libros.push(nuevoLibro)
    // localStorage.setItem(key,value)
    // localStorage.setItem("titulo",nuevoLibro.titulo)
    // localStorage.setItem("autor",nuevoLibro.autor)

    let librosJSON = JSON.stringify(libros)
    localStorage.setItem("data",librosJSON)

    //recorrer el array
    //template string -> tilde invertida o backticks
    for (const i of libros) {
        // contenedor.innerHTML+="<div>"+i.autor+i.titulo+"</div>"
        contenedor.innerHTML+=`
        <div class='libro'>
            <div class='data'>
                <h3>${i.titulo}</h3>
                <p>${i.autor}
                <br>${i.lanzamiento}
                <br><span class='cant'>stock: ${i.stock}</span>
                </p>
            </div>
            <div class='icon'>
                <span>📚</span>
            </div>
        </div>
        `
    }

    //borramos los campos
    formCarga.reset()
}

function borrarLibros(){
    contenedor.innerHTML=""
    // libros.pop()
}

function recuperarData(e){
    e.preventDefault()
    // let leerJSON = JSON.parse(localStorage.getItem("data"))
    let infoJSON = localStorage.getItem("data")
    let leerJSON = JSON.parse(infoJSON)
    // console.log(leerJSON)

    contenedor.innerHTML=""

    for (const i of leerJSON) {
        contenedor.innerHTML+=`
        <div class='libro'>
            <div class='data'>
                <h3>${i.titulo}</h3>
                <p>${i.autor}
                <br>${i.lanzamiento}
                <br><span class='cant'>stock: ${i.stock}</span>
                </p>
            </div>
            <div class='icon'>
                <span>📚</span>
            </div>
        </div>
        `
    }
}

//ejecutar la funcion de carga, por medio de un evento -> addEventListener(evento,funcion)

formCarga.addEventListener("submit",cargarLibro)

let linkJSON = document.getElementById("json")
linkJSON.addEventListener("click",recuperarData)

let btnBorrar = document.getElementById("borrar-libros")
btnBorrar.addEventListener("click",borrarLibros)







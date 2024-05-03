
//Crear la clase libros

class Libros {
    constructor(tit,aut,lan,sto){
        this.titulo=tit,
        this.autor=aut,
        this.lanzamiento=lan,
        this.stock=sto
    }
}
//1 - Creacion manual
const libro1 = new Libros("Cuentos","R.Fontanarrosa",1970,35)
const libro2 = new Libros("Otros cuentos","Borges", 1940, 23)
const libros = []
libros.push(libro1,libro2)

//2 - Creacion por medio de funciones
function crearLibro1(tit,aut,lan,sto){
    const nuevoLibro = new Libros(tit,aut,lan,sto)
    libros.push(nuevoLibro)
}
// crearLibro1("Cuentos","R.Fontanarrosa",1970,35)
// crearLibro1("Otros cuentos","Borges", 1940, 23)
// crearLibro1("mas cuentos","E.Sacheri",2006,67)

let contenedor = document.querySelector("#libros-oferta")
for (const i of libros) {
    contenedor.innerHTML+="<div>"+i.autor+"</div>"
}
//Definimos la Clase Libro
class Libro {
    constructor(tit,aut,lan,sto){
        this.titulo=tit
        this.autor=aut
        this.lanzamiento=lan
        this.stock=sto
    }

}
//Creamos una instancia de Libro

let libro1 = new Libro("Rayuela","J.Cortazar",1950,56)
let libro2 = new Libro("harry potter y ...", "JK Rowling", 1996, 57)

libros.push(libro1,libro2)

for (const iterator of libros) {
    contenedorLibros.innerHTML+=iterator.titulo+" "+iterator.autor+" "+iterator.lanzamiento+"<br>"
}
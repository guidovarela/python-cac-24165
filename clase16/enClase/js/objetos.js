// objetos
    // propiedad
    // objeto.propiedad

let persona = {
    nombre:"Jose",
    apellido:"Lopez",
    edad:30,
    mascotas:["tobi","manchita","negra"],
    nombreCompleto: function () {
        return this.nombre +" "+this.apellido
    }
}


//DOM - Document Objet Model
let caja = document.querySelector("#persona")

// let data = caja.innerHTML="Mi nombre es "+persona.nombreCompleto()+"<br>Tengo "+persona.edad+".<br>Tengo "+persona.mascotas.length+" mascotas."

// array de Objetos

let libros = [
    {
        titulo: "El Gran Gatsby",
        autor: "F. Scott Fitzgerald",
        añoPublicacion: 1925
    },
    {
        titulo: "Cien años de soledad",
        autor: "Gabriel García Márquez",
        añoPublicacion: 1967
    },
    {
        titulo: "1984",
        autor: "George Orwell",
        añoPublicacion: 1949
    },{
        titulo:"El señor de los anillos",
        autor:"JRR Tolkien",
        añoPublicacion: 1955
    }
];

for (data of libros) {
    caja.innerHTML+="<div>"+data.titulo+"</div>"
}
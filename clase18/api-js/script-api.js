
let store = document.querySelector(".store")
let products = document.querySelector(".products")
let categories = document.querySelector(".categories")

let titleHead = "Tienda"
let subtitleTag = document.getElementsByTagName("h2")
let titleTag = document.getElementsByTagName("title")
subtitleTag[0].innerHTML=titleHead
titleTag[0].innerHTML=titleHead


async function getOpenLibraryAPI(){
    let url = "https://openlibrary.org/search.json?q=the+lord+of+the+rings"
    let respuesta = await fetch(url)
    // console.log(respuesta.status)
    // console.log(respuesta.statusText)

    let data = await respuesta.json()
    // console.log(data.docs)

    products.innerHTML=""

    data.docs.forEach(libros => {
        products.innerHTML+=`<div class="data"><p>${libros.author_name[0]} - <br> 1era publicacion: ${libros.first_publish_year}</p></div>`
    });
}

 const getCategories_FakeShopAPI = async () => {
    let url = "https://fakestoreapi.com/products/categories"
    let respuesta = await fetch(url)
    // console.log(respuesta.status)
    // console.log(respuesta.statusText)
        .then(res=>res.json())
        .then(json=>{
            
            let categoryNames = document.createElement("div")
            categoryNames.className="categoria"
            categories.append(categoryNames)

            console.log(categories)
            console.log(json)
            for (const i of json) {
                categories.innerHTML+=`<button href="#" >${i}</button>`
            }

        })
}

async function getFakeShopAPI(){
    let url = "https://fakestoreapi.com/products"
    let respuesta = await fetch(url)
    // console.log(respuesta.status)
    // console.log(respuesta.statusText)
        .then(res=>res.json())
        .then(json=>{
            // console.log(json)

            products.innerHTML=""
            for (const i of json.reverse()) {
                products.innerHTML+=`
                <div class='data'>
                    <div class='category'>
                        <span>
                            ${i.category}
                        </span>
                    </div>
                    <div class='img'>
                        <img src="${i.image}"}
                    </div>
                    <div class='title'>
                        ${i.title.substring(0, 20)}
                    <div>
                    <div class='price'>
                        $ ${i.price}
                    </div>
                 <div>`
            }
        })
        
}
// getOpenLibraryAPI()
getFakeShopAPI()
getCategories_FakeShopAPI()

products.innerHTML=`<div class='loading'><img src="loading.gif"></div>`

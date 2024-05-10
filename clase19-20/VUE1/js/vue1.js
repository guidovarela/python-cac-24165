        //const createApp = new Vue;

const { createApp, ref } = Vue
createApp({
setup() {
    let message = '<h2>Hello vue!</h2>'
    
    return {
    nombre: "Mario",
    apellido: "Baracus",
    message
    }
}
}).mount('#app')
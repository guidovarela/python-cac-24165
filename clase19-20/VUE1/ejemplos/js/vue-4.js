

const componente1 = {
    template: `<h4 class="">Curso: {{usuario}}</h4><p>{{anio}}</p>`,
    data() {
        return { usuario: "Codo a Codo 4.0", anio:2024 }
    }
 }
 

const {createApp} = Vue 
createApp({
    data(){
        return{
            frutas:[
                {nombre:"Manzana", cantidad:50},
                {nombre:"Uva", cantidad:75},
                {nombre:"Mango", cantidad:96},
                {nombre:"Frutilla", cantidad:45}
            ]
        }
    },
    // Funciones de data binding
    // methods: {
    //     agregarFruta() {
    //         this.frutas.push({ nombre: this.nuevaFruta, cantidad: 0 })
    //         console.log(frutas)
    //     }
    // },
    
    components:{
        info: componente1 
    }
    
}).mount("#app")
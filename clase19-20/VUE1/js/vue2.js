        //const createApp = new Vue;

const { createApp } = Vue
createApp({
    setup() {  
        let productos = [
            {nombre:"libro", cantidad:10},
            {nombre:"botella", cantidad:75},
            {nombre:"leopardo", cantidad:96},
            {nombre:"laptop", cantidad:45}
        ]  

        return {
            productos
        }
    }
}).mount('#data')
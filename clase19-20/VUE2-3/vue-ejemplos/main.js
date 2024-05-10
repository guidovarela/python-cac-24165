let app = {
    data(){
        return {
            temario : ['aplicaciones reactivas', 'propiedades computadas','watchers', 'accesos a la DOM con refs','modelo mvc', 'modelo mvvm'],
            pedidos:[],
            pedido:{
                nombreProducto: null,
                precioProducto: null,
                cantidad:null
            },
            cssValue:false,
            value:null,
            cambio: null,
            siCambia:null,
            totalPedidos:null
        }
    },

    methods:{
        agregarPedido(pedido){
            //hay que hacer una copia del pedido para que lo tome como valor a ingresar
            this.pedidos.push({...pedido});
            
        },
        changeBackGround(){
            this.cssValue = ! this.cssValue;
        },
        renderValue(data){
            console.log(data.path[0].value);
            this.value = data.path[0].value;

        }
    },

    computed:{
        totalTemario:function(){
            return this.temario.length
        }
    },
    watch:{
        pedidos: {
        handler(value){
            if(value.length >3 ){
            this.totalPedidos = value.length}
        },
        deep:true
    }
}


}

const appRoot= Vue.createApp(app).mount('#app') ;

// Objeto de VUE!!!
console.log(Vue)

const app = Vue.createApp({
  // Estamos usando OPCIONES!!!!
  // Cada cosa es una opcion, por eso es la option API: template, data, methods, computed, etc
  // cada parte es una opcion!!!

  // podemos crear el template a mostrar
  // template: `
  //   <h1>Hola mundo</h1>
  //   <p>Desde app.js</p>
  //   <!-- Reprsentación declarativa -->
  //    <p>{{1+1}}</p>
  //   `,

  // Función que maneja nuestro estado y este es reactivo
  data: () => ({
    message: 'Mi variable de mensaje :)',
    clic:0,
    heroes: [
      {
        id: 1,
        name: 'Ironman',
      },
      {
        id: 2,
        name: 'Capitan America',
      },
      {
        id: 3,
        name: 'Hulk',
      },
    ],
    newHero: '',
    saludo: "Hola Mundo!"
  }),

  // Mis metodos
  methods: {
    changeMessage() {
      this.message = 'Has pulsado el botón'
    },
    addHero() {  
      this.heroes.push({
        id: this.heroes.length + 1,
        name: this.newHero,
      })
      this.newHero = ''
    }
  },
})

app.mount('#myApp')

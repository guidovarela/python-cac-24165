 //comentario linea simple
        /*
        comentario
        multi
        linea
        */

        // variables -> espacio de memoria, permite variacion de dato
        //  datos a partir de su tipo de dato
        // var - let - const
    
        let saludo = "no hay mas saludos..." 
        console.log(saludo)
        console.log("2" + 2 * true)

        saludo = 23
        // alert(saludo)

        const pi = 3.14159
        console.log("El valor de pi es: "+pi)

        // tipos de datos
        let nombre = "Guido"
        let edad = 43
        let esHumano = true

        console.log(typeof(nombre))

        // Cuadros de dialogo
        // alert() prompt() confirm()
        let num1 = parseFloat(prompt("inserta 1 numero:")) 
        let num2 = parseFloat(prompt("inserta 1 numero:"))
        // console.log(parseInt(num1) + parseInt(num2)) 
        console.log(num1 + num2) 
        console.log(num1 - num2) 
        console.log(num1 * num2) 
        console.log(num1 / num2) 

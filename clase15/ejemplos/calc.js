
    
let btnCalc = document.getElementById('btn-calc')
btnCalc.addEventListener("click", function(){
        //ubicar los objetos (datos)
        let signo = document.querySelector('#signo').value
        let resultado = document.getElementById('resultado')
        let op 
            //convertir en numericos/decimales, los datos string
            let num1 = parseFloat(document.querySelector('#num1').value)
            let num2 = parseFloat(document.querySelector('#num2').value)

    //validar si los campos estan vacios - TAREA
    if(num1 == "" || num2 == ""){
        resultado.innerHTML = "Debes ingresar dos números para comenzar"
    }else{
        //comparar los signos, y realizar operacion matematica
        if(signo === "+"){
            //insertar el resultado
            op = num1 + num2
            resultado.innerHTML = `${num1} ${signo} ${num2} = ${op}`
            console.log(num1)
            console.log(num2)
        }else if(signo === "-"){
            op = num1 - num2
            resultado.innerHTML = `${num1} ${signo} ${num2} = ${op}`
        }else if(signo === "/"){
            // si num2 es 0 -> error - TAREA
            op = num1 / num2
            resultado.innerHTML = `${num1} ${signo} ${num2} = ${op}`
        }else{
            op = num1 * num2
            resultado.innerHTML = `${num1} ${signo} ${num2} = ${op}`
        }
    }

})

//borrar resultados
let btnReset = document.getElementById('reset-calc')

btnReset.addEventListener("click", function(){
    resultado.innerHTML = ""
})
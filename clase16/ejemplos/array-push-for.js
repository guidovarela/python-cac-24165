let data= ["perro","gato","elefante"]

function agregarItem(animal){
	data.push(animal)
}
function quitarItem(animal){
	data.unshift(animal)
}

agregarItem("raton")
agregarItem("Leon")
quitarItem("tigre")

for (datos of data){
	document.write(datos+"<br>")
}
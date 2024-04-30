// Obtener el elemento de entrada de texto (input) y el botón de guardar
const entradaNombre = document.getElementById('nombre');
const botonGuardar = document.getElementById('boton-guardar');
const mensajeBienvenida = document.getElementById('mensaje-bienvenida');

// Verificar si hay un nombre guardado en localStorage
const nombreGuardado = localStorage.getItem('nombre');

// Mostrar un mensaje de bienvenida si el nombre está guardado
if (nombreGuardado) {
    mensajeBienvenida.textContent = `Bienvenido ${nombreGuardado}`;
}

// Manejar el evento de clic en el botón de guardar
botonGuardar.addEventListener('click', () => {
    // Obtener el nombre ingresado en el campo de entrada de texto
    const nombre = entradaNombre.value;
    
    if (nombre !== '') {
        // Guardar el nombre en localStorage
        localStorage.setItem('nombre', nombre);

        // Mostrar un mensaje de bienvenida con el nombre ingresado
        mensajeBienvenida.textContent = `Bienvenido ${nombre}`;
    } else {
        // Mostrar un mensaje de error si no se ingresó un nombre
        alert('Por favor ingresa tu nombre.');
    }
});

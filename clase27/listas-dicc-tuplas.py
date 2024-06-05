# Lista de números
numeros = [1, 2, 3, 4, 5]

# Diccionario que almacena información de una persona
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ciudad de Buenos Aires"
}

# Tupla que almacena coordenadas
coordenadas = (10.0, 20.5)

# Acceder a elementos de una lista
primer_numero = numeros[0]  # Acceder al primer elemento (índice 0)
ultimo_numero = numeros[-1]  # Acceder al último elemento (índice -1)

# Acceder a valores de un diccionario
nombre_de_persona = persona["nombre"]
edad_de_persona = persona["edad"]

# Desempaquetar valores de una tupla
x, y = coordenadas  # Desempaquetar las coordenadas en x e y

# Modificar elementos de una lista
numeros[2] = 100  # Cambiar el tercer elemento a 100

# Agregar elementos a una lista
numeros.append(6)  # Agregar el número 6 al final de la lista

# Modificar valores en un diccionario
persona["ciudad"] = "Nueva Ciudad"  # Cambiar la ciudad de la persona

# Crear una tupla con valores constantes que no se pueden modificar
punto_fijo = (0, 0)

# Longitud de una lista
longitud_lista = len(numeros)  # Devuelve 6 en este caso

# Comprobar si una clave existe en un diccionario
existe_clave = "apellido" in persona  # Devuelve False, ya que "apellido" no existe

# Iterar a través de una lista
for numero in numeros:
    print(numero)

# Iterar a través de un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Usar una tupla para devolver múltiples valores desde una función
def obtener_coordenadas():
    return (30.0, 40.5)

x, y = obtener_coordenadas()
print(f"Coordenadas: x = {x}, y = {y}")

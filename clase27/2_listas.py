""" 
    Listas: es una secuencia ordenada de elementos.
    Las listas en Python son un tipo contenedor, 
    y se usan para almacenar conjuntos de elementos relacionados.
    
    Acceso a los elementos por indice.
    logintud len()
    Iterar una lista numérica y sumar sus elementos
    Sumar elementos sum()
    Funciones min(), max(), list(), sort()
    Mostrar indice y elemento
    Operadores de pertenecia int, not in
    métodos: append(), count(), 

    Tipo de dato mutable
    
"""

elementos = []
numeros = [1,2,3,4,5] 
dias = ["Lunes", "Martes", "Miércoles"] 
vocales = "aeiou"

# Agregar elementos
print(elementos)
elementos.append(True)
elementos.append(False)
print(elementos)

longitud = len(numeros)
print(longitud)

# numeros = [1,2,3,4,5] 

suma = 0
for numero in numeros:
    suma += numero

print("Resultado", suma)

print(sum(numeros))
print(min(numeros))
print(max(numeros))

# dias = ["Lunes", "Martes", "Miércoles"] 

print(dias[0])
print(dias[2])

print(dias[1:3])   #['Martes', 'Miércoles']
print(dias[-2:])  #['Martes', 'Miércoles']
print(dias[2:3]) # ['Miércoles']


# vocales = "aeiou"
lista_vocales = list(vocales)
print(lista_vocales)

#dias = ["Lunes", "Martes", "Miércoles"] 
print("Jueves" in dias) # False
print("Viernes" not in dias) # True


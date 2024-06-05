# Declaración de listas (arrays)
numeros= [] # Lista vacía
numeros= [2,5,-2,10,10,1]
palabras= ["a", "hola", "Juan", "", "ABC", "123!"]
'''
# Mostrar una lista
print(numeros)

# Cantidad de elementos de una lista (len)
print(len(numeros))
print(len(palabras))

# Acceder a una posición
print(numeros[0])

# Imprimir una lista
for i in range(len(numeros)):
    print(numeros[i])

for i in range(0, len(palabras), 1): # 0 1 2 3 4 5
    elem= palabras[i]
    print("Posición:", i, "Valor:", elem)

# Iterar sobre una lista
for valor in numeros:
    print(valor, end=" ") # Mostrar una lista en la misma línea

# Modificar un valor en una posición
print(numeros)
numeros[0]= 100

# Agregar un elemento
# numeros.append(60) # Al final
# numeros= numeros + [60,61]
numeros.extend([60,61])

# Ejemplo de sumar 2 listas
numeros1= [1,2,3]
numeros2= [6,10,-2]
numeros3= numeros1 + numeros2
print(numeros3)

# Eliminar
print(numeros)
numeros.pop() # el último elem.
# pos= 1 
# numeros.pop(pos)
del(numeros[1])
print(numeros)

# Ejemplo: eliminar todos los elem. pares (valor) de una lista
for i in range(len(numeros)):
    num= numeros[i]
    if num%2==0:
        numeros.pop(i)
print(numeros)

i= 0
while i<len(numeros):
    num= numeros[i]
    if num%2==0:
        numeros.pop(i)
    else:
        i+=1
print(numeros)
for i in range(len(numeros)-1, -1, -1):
    num= numeros[i]
    if num%2==0:
        numeros.pop(i)
print(numeros)

# Insertar valores
print(palabras)
palabras.insert(1, "Ramiro")
print(palabras)
'''

# Ordenar listas
print(numeros)
numeros.sort(reverse=True)
print(numeros)
print(palabras)
palabras.sort()
print(palabras)

# Matriz de 2x2
matriz= [
    [1,2],
    [3,4]
]
print(matriz)

# Mostrar una lista por pantalla
for fila in matriz:
    print(fila)

print(matriz[0][0])

# sum, count
print(sum(numeros))
print(numeros.count(10)) # 2

# https://www.w3schools.com/python/python_lists.asp

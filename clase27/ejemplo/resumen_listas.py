# Declarar listas (dinámicas)
numeros= [] # lista vacía
numeros= [1,2,3,50,0,-34]
palabras= ["A","KIWI","MANZANA"]

print(numeros)

# to-do: crear fx para mostrar una lista
for valor in numeros:
    print(valor, end= " ")
print()

print(len(numeros))
print(palabras[2])
# Modifico una lista
palabras[2]= 'FRUTILLA'
print(palabras)

# Ejemplo: modificar una lista de números (x2)
for i in range(len(numeros)): # 0 1 2 ... 5
    # print(numeros[i], end= " ")
    numeros[i]= numeros[i]*2
print(numeros)

# MOSTRAR una caracter de un elem. dentro de una lista
palabra= palabras[2]
print(palabra)
print(palabra[0])
print(palabras[2][0])

# Agregar un elem.
palabras.append('123')
# Insert
palabras.insert(0, '456')
print(palabras)
# Eliminar
palabras.pop()
palabras.pop(0)
print(palabras)
# Eliminar por elemento
# palabras.remove('1') # ValueError
palabras.remove('A') # ValueError
print(palabras)

# Ordenar listas
numeros.sort()
numeros.sort(reverse=True)
print(numeros)

# Más métodos
# sum y count
print(sum(numeros))
print(numeros.count(100))

# Matrices
# matriz de 2x2
m= [
    [1,2],
    [3,4]
    ]
print(m[1][1])
print(m)
# m.pop(0)
print(m)
m[1].pop()
print(m)

# aleatorios
print(type(m)) # <class 'list'>

# https://www.w3schools.com/python/python_lists.asp

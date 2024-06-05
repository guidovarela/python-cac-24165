# Diccionarios
dicc= {"Ramiro":39, "Juan":17, "Pedro":18}
print(dicc)
print(dicc["Ramiro"])

# Mostrar los mayores de edad
for clave in dicc:
    if dicc[clave]>=18:
        print(clave, "es mayor de edad.")

# Muestro todas las edades
for valor in dicc.values():
    print(valor)

# Tuplas
fecha= (2020,12,21)
print(fecha)
# Desempaquetado
anio, mes, dia= fecha
print(anio)
print(mes)
print(dia)
# Agrupo info en un tupla
tupla_verano= (21, "Diciembre", "Verano")
print(tupla_verano[2])

for elem in tupla_verano:
    print(elem)

# Aplico rebanadas a una tupla
print(tupla_verano[0:2])
print(tupla_verano[0:1])
print(tupla_verano[:]) # copiar una tupla

# Conjuntos: eliminar repetidos
ejemplo_conjunto= {-1, 3, 4, 5}
lista= [1,1,2,3,4,5]
conjunto= set(lista)
print(conjunto)
nueva_lista= list(conjunto)
print(nueva_lista)

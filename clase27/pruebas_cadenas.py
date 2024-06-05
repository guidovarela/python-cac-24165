x = ""
x = """Esto 
es una
cadena"""

"""Comentario"""

nombre = "Jose "
# print(len(nombre))
# print(nombre[4])

# unir
apellido = "Velez"
nombreCompleto1 = nombre + apellido
nombreCompleto2 = nombre.join(apellido)

# listas -> arreglo / matriz


numeros = [2,3,4,5,56,43,7,12,45,1] 
# print(numeros[-1]) # ultimo indice
# print(len(numeros))

# for i in range(10):
# for i in range(0,len(numeros),1):
#     # suma = suma + numeros[i]   
#     print(numeros[i])

# print(i) 
  
""" i = 0
suma = 0
while i < len(numeros):
    suma = suma + numeros[i]  
    i += 1
print(suma) """

# Agregar data
# dias = ["Lunes", "Martes", "Miércoles"]
# nuevodia = input("Agregar dia: ")

# dias.append(nuevodia)

# for i in range(len(dias)):
#     print(dias[i])


# Diccionarios -> AKA objetos
# nombre = {key:item,key:item}
data  = {'Juan': 56, 'Ana': 15, 'Julia': 25, 'Nina':46}
# print(f"Juan tiene {data['Juan']}")

# print("Keys:",data.keys())
# print("Items:",data.items())

for i in data.keys():
    print(data[i])

for clave,valor in data.items():
    print(clave)
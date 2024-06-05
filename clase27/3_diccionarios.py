"""
    Diccionarios: son un conjunto no ordenado de pares ->clave: valor. 
    Estas claves son únicas, y si se intenta guardar un valor a una
    clave ya existente se pierde dicho valor. 
    
    {key, value}
    Acceso a los valores por su clave
    Iterar un diccionario, mostrando key and value
    Calcular promedio de edad

"""
diccionario1 = {}
diccionario2  = {'Juan': 56, 'Ana': 15, 'Julia': 25, 'Nina':46}

print(diccionario1)
diccionario1["carne"] = 50
diccionario1["pollo"] = 75
diccionario1["humita"] = 30
print(diccionario1)

print("Juan tiene:",diccionario2['Juan'])
print("Nina tiene:", diccionario2['Nina'])
print("Nina tiene:", diccionario2.get("Nina"))

#print("Lolo tiene:", diccionario2['Lolo'])
print("Lolo tiene:", diccionario2.get("Lolo","No existe"))


for k,v in diccionario2.items():
    print(f'Nombre: {k}, edad{v}')

#diccionario2  = {'Juan': 56, 'Ana': 15, 'Julia': 25, 'Nina':46}

print(diccionario2.values())
print(diccionario2.keys())

# edades es una lista
edades = diccionario2.values()
suma = sum(edades)
cantidad = len(edades)

promedio = suma/cantidad
print(f'El promedio de edades es:{promedio}')
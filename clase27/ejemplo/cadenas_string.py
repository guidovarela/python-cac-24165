cadena= "   Hol@ Mundo 123!   "
print(cadena)
'''
print(len(cadena))
print(cadena[0])
print(cadena[4])
# cadena[0]= "h" # NO mutable

# Buscar una subcadena
print(cadena.find("M")) # 5
print(cadena.find("Mundo")) # 5
print(cadena.find("123")) # 11
print(cadena.find("$")) # -1

# Itero sobre la cadena
for car in cadena:
    print(car)

# Itero sobre la cadena
for car in cadena:
    # if car.isnumeric(): # imprimo sólo numéricos
    # if car.isalpha(): # imprimo sólo alfabéticos
    # if not car.isalpha() and not car.isnumeric(): # NO imprimo alfabéticos ni números
    if not (car.isalpha() or car.isnumeric()): # NO imprimo alfabéticos ni números
        print(car)
'''

# Reemplazar una subcadena
cadena2= cadena.replace("Mundo", "Otra subcadena")
print(cadena)
print(cadena2)

# upper, lower, strip
print(cadena.upper()) # HOL@ MUNDO 123!
print(cadena.lower()) # hol@ mundo 123!
print(cadena.strip()) # Hol@ Mundo 123!
print(cadena.rstrip()) # Hol@ Mundo 123!
print(cadena.lstrip()+"---") # Hol@ Mundo 123!

# https://www.w3schools.com/python/python_ref_string.asp

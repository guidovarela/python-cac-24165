""""

    Ejemplo: condicional simple if

    condicional compuesto
    
    condicional anidado
    
    condicional elif
    
Simple
"""
""" numero = float(input("Ingrese un número: "))
if numero > 0:
    print("Soy positivo")
 """


# Compuesto
# numero = float(input("Ingrese un número: "))

# if numero > 0:
#     print("Soy positivo")
# else: 
#     print("Soy negativo o igual a cero")

# Anidado
# numero = float(input("Ingrese un número: "))
# if numero > 0:
#     print("Soy positivo")
# else: 
#     if numero < 0:
#         print("Soy negativo")
#     else:
#         print("Soy igual a cero")


# elif
numero = float(input("Ingrese un número: "))
if numero > 0:
    print("Soy positivo")
elif numero < 0:
    print("Soy negativo")   
else:
    print("Soy igual a cero")
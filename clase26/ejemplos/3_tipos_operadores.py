""""

    Ejemplo: operadores aritméticos
    suma +
    resta -
    multiplicación *
    división /
    división exacta //
    resto %
    potencia **
    
    operadores de asignación compuestos
    suma +=
    resta -=
    multiplicación *=
    división /=
    división exacta //=
    resto %=
    potencia **=

    Operadores de pertenencia
    in 
    not in
"""
#nombre_apellido = "Polo José"

num1 = 8
num2 = 4
print(f'La suma entre {num1} y {num2} es: {num2+num1}')
print(f'La resta entre {num1} y {num2} es: {num2-num1}')
print(f'La división entre {num1} y {num2} es: {num2/num1}')
print(f'La división entera entre {num1} y {num2} es: {num2//num1}')
print(f'La resto entre {num1} y {num2} es: {num2%num1}')
print(f'La potencia entre {num1} y {num2} es: {num2**num1}')

print("Antes", num1)
num1 += num2  # num1 = num1 + num2
print("Despúes", num1)

print("Antes", num1)
num1 -= num2  # num1 = num1 + num2
print("Despúes", num1)

print("Antes", num1)
num1 *= num2  # num1 = num1 + num2
print("Despúes", num1)

# Operadores de pertenecia

cadena = "Codo a codo"
# print("z" in cadena)
# print("o" in cadena)

print("z" not in cadena)
print("o" not in cadena)
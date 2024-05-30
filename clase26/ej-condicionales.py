# Estructura condicional simple
'''
Ingresar el sueldo de una persona, si supera los 500000 pesos, mostrar un mensaje en
pantalla indicando que debe abonar impuestos.

topeSueldo = 500000
sueldo=int(input("ingresar su sueldo: "))

if sueldo > topeSueldo:
    print("Debe abonar impuestos 😡)")
else:
    print("Zafaste 😁)")
'''

# def calcularIG(tope):
#     sueldo=float(input("ingrese su sueldo:"))
#     if(sueldo!=0 and sueldo < tope):
#         print("No vas a pagar el impuesto 😁")
#     else:
#         print("Lamento la noticia: tenes que pagar 😫")


# Estructura condicional doble
'''
Realizar un programa que solicite ingresar tres números distintos y muestre por pantalla el mayor de ellos.
'''
# num1=None
num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese otro número (distinto): "))
num3= int(input("Ingrese otro número (distinto): "))
if num1!=num2 and num2!=num3 or num3!=num1:
    if num1>num2 and num1>num3: # Bloque de verdad
        print("num1 es mayor.")
    elif num3>num2:
        print("num3 es mayor.")
    else: # Bloque de falsedad
        print("num2 es mayor.")
else:
    print("Error! Los números NO son distintos!")


'''
Operadores logicos:
if user==None or pass==None:
    # bloque verdadero
if user!=None and pass!=None:
    # bloque verdadero
'''
    

# Estructuras condicionales anidadas
'''
determinar que no sean iguales y luego compararlos
'''

# if-else-elif
'''
Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el
promedio e imprima alguno de estos mensajes:
    Si el promedio es >=7 mostrar "Promocionado".
    Si el promedio es >=4 y <7 mostrar "Regular".
    Si el promedio es <4 mostrar "Reprobado".
    Agrego a la consigna: Si el promedio es entre 3 y 4 -> Recupera

'''

# Estructura condicional múltiple/Alternativa Múltiple 


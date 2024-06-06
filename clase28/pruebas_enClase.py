# saludo = "Hola!"
# def saludar():
#     print(saludo)

# saludar()



def imprimir_mensaje_arg(cant,mens):
    for i in range(cant):
       print(mens + str(i))

# imprimir_mensaje_arg(int(cantidad),"Mensaje nro: ")

cantidad = "4"

mensaje = "Mensaje nro: " 
def imprimir_mensaje():
    cant = int(input("Cuantas veces?"))
    for i in range(cant):
        print(mensaje + str(i+1))
# imprimir_mensaje()

# Invocación de la función
def imprimir_mensaje_N_veces(n, m):
   for i in range(n):
       print(m)

# mensaje = input("Mensaje: ")
# veces = int(input("Nro. de veces que desea imprimir: "))
# imprimir_mensaje_N_veces(veces, mensaje)

# Devolucion de valores -> return
# variables de ambito global

def restar(num1,num2):
    # variables de ambito local
    return num1-num2
   #return resta  Retorna un valor

resta = restar(30,20)
# print(resta)
# imprimir_mensaje_arg(resta,"resultado de una resta")


# Programa principal
# print(f'El Resultado es: {restar(10,5)}')


""" Funciones de tablas de multiplicar """

# 1- Genera la tabla del "n"
def calcular(n):
   tabla = []
   for i in range(1,11):
       tabla.append(f"{n}x{i}={n*i}")
   return tabla

# res_tabla = calcular(2)
# for i in range(len(res_tabla)):
#     print(res_tabla[i])

# 2- Muestra en terminal la tabla elegida
def calcular_tabla(i):
    print(f"Tabla del {i}:")
    tabla = calcular(i)
    for res in tabla:
        print(res)
    # print("-"*cant)
# calcular_tabla(5)

# 3- Muestra en terminal todas las tablas
def calcular_todas(inicio,fin):
   for i in range(inicio,fin):
       print(f"Tabla del {i}:")
       tabla = calcular(i)
       for j in tabla:
           print(j)
       print("-"*10)

calcular_todas(1,8)
# calcular_tabla(int(input("De que numero queres ver la tabla?")))


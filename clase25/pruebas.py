"""
Comentario multilinea
DOS 

cd
dir
dir/w
cd..

"""

# print("Estamos usando Python") # comentario

#variables
nombre = "Elvis" #str
numeric = "10" #int
floatNum = 13.2 # float
dataLogic = False # boolean

# print("Mi nombre es "+nombre+", tengo "+numeric+" hermanos")
# print(f'mi nombre es {nombre}, tengo {numeric} hermanos')
# print("Mi nombre es",nombre)

# print(int(numeric) + 10)

# funcion
"""
def nombreFuncion():
    scope o instucciones

"""
def saludar():
    saludo = input("Escribe tu nombre")
    print(f'Hola {saludo}, mi nombre es {nombre}')


"""
condicionales
if(condicion):
    # verdadero
else:
    #falsa
"""
def necroElvis():
    print("Estado de vida:")
    print("inserte 1 si esta vivo")
    print("inserte 0 si esta muerto")
    estado = int(input())
    if estado == 1:
        print(f'{nombre} esta vivo')
    else:
        print(f'{nombre} esta muerto')
necroElvis()

numero1=10

def comprobar():
    if(numero1 == 1):
        print(numero1*10)
    elif(numero1 == 3):
        print(numero1+3000)
    else:
        print(numero1-3000)

# Estructuras Iterativas/Repetitivas
# Ciclo Exactos: se sabe la cantidad exacta de repeticiones (while/for).
# Ciclo Condicionales: no se determina la cantidad de repeticiones (while).

# Ciclo Exactos
'''
Realizar un programa que imprima en pantalla los números del 1 al 100.

i= 1 # Inicialización del contador
N= int(input("Ingrese valor máximo del contador: "))
while i<=N: # Planteo una condición (que en algún momento tiene que finalizar)
    print(i) # El orden es importante
    i+=1 # * # Importante: evitar ciclos infinitos
'''

# Ciclo Condicionales: no se la cantidad de repeticiones (while).
'''
Realizar un programa que calcule la sumatoria de números enteros ingresados
por teclado. Finaliza el programa ingresando 0.

suma= 0 # Inicializo mi acumulador (sumatoria)
num= int(input("Ingrese un número:"))
while num!=0:
    # suma= suma+num
    suma+= num
    num= int(input("Ingrese otro número (o 0 para finalizar): "))
print("La sumatoria de los números ingresados es:", suma)
'''

# Ciclo Exactos: yo se la cantidad exacta de repeticiones (for).
'''
Realizar un programa que imprima en pantalla los números del 1 al 100.

N = int(input("Ingrese el valor máximo del contador: "))

for i in range(1,N+1,2): # (inicio, fin, incremento/salto)
    print(i)
'''

'''
Confeccionar un programa que pida insertar notas de un alumno, y luego imprima las notas y el promedio
'''
""" cantNotas = int(input("Cuantas notas vas a cargar ?(ingresar numero):"))
sumNotas = 0
for notas in range(cantNotas):
    nota = int(input(f'Ingrese nota {notas+1}: '))
    sumNotas += nota
    promedio= sumNotas / cantNotas
    print(f'Nota {notas+1}: {nota}')

print(f"Promedio de {cantNotas} notas:", promedio) """


# for in -> listas (arrays)
frutas = ["manzana", "plátano", "uva", "naranja"]

cont=0

for i in frutas:
    cont+=1
    print(f"Fruta {cont}: {i}")
print(f'Cantidad de frutas: {len(frutas)}')




'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(numero, "es par")
    else:
        continue
    print("Esta línea se ejecutará solo si el número es par.")
    
    if numero == 6:
        break
'''
""""

    Ejemplo: ciclo while
    solicitar 3 números y sumarlos
    
"""

contador = 0
sumatoria = 0

while contador <=3:
    numero = float(input("Ingrese un número:"))
    sumatoria += numero
    contador += 1

print("Resulatdo:", sumatoria)

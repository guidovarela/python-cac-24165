"""
    Conjuntos: son conjuntos de elementos únicos, no ordenados 
    y sus elementos no son mutables. Se definen sus elementos
    encerrándolos entre llaves y separados por comas.

    Crear un conjunto set([listado])
    Iterar un conjunto

"""

# Vacío
conjunto1 = {}
conjunto2 = set()

# Con elementos
conjunto3 = {'Fernando', (13, 11, 1985), 37}

# Crear conjunto
conjunto4 = set([1,2,2,2,3,4,4,5])
print(conjunto4)

for elem in conjunto3:
    print(elem)


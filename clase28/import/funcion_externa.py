# Craer una función que genere una lista de n elementos
# indicado por parámetros
# los números de los elementos deben estar entre 1 y 10

import random

def crear(cantidad):
    """ Recibe un número que representa 
    la cantidad de elementos que tendrá 
    la lista """

    lista = []
    for i in range(cantidad):
        lista.append(random.randint(1,10))
    
    return lista

def saludar():
    print("esto esta en otro archivo!")

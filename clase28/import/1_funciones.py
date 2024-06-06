# FORMA N1 DE IMPORTAR UNA FUNCIÓN DE OTRO ARCHIVO
# import funcion_externa
# lista = funcion_externa.crear_lista(6)
# print(lista)

# FORMA N2
from funcion_externa import crear,saludar

lista = crear(3)
for i in range(len(lista)):
    print(lista[i])

saludar()

from modFunciones import agregar_producto,mostrar_productos

# Preguntar al usuario cuántos productos desea cargar
num_productos = int(input("¿Cuántos productos desea cargar? "))
lista_productos = []

# Solicitar y agregar los productos a la lista
for i in range(1, num_productos + 1):
    agregar_producto(lista_productos, i)

# Mostrar la lista de productos
mostrar_productos(lista_productos)


# Importamos las funciones desde el modulo 'modFunciones'
from modFunciones import agregar_producto,mostrar_productos,mostrar_productos_iva,aplicar_descuento_y_leyenda

# from modFunciones import * -> importar todo
# from carpeta.modFunciones import * -> desde un directorio
# from carpeta.modFunciones import as def1,def2,def3,def4 -> alias


# Preguntar al usuario cuántos productos desea cargar
num_productos = int(input("¿Cuántos productos desea cargar? "))
lista_productos = []

# Solicitar y agregar los productos a la lista
for i in range(1, num_productos + 1):
    agregar_producto(lista_productos, i)

# Mostrar la lista de productos
mostrar_productos(lista_productos)

# Permitir al usuario elegir un producto por número para aplicar el descuento o ver el IVA
numero_elegido = int(input("Elija un producto por su número para aplicar el descuento (0 para salir): "))
while numero_elegido != 0:
    if 1 <= numero_elegido <= len(lista_productos):
        producto_elegido = lista_productos[numero_elegido - 1]
        aplicar_descuento_y_leyenda(producto_elegido)
        print(f"Descuento aplicado al producto #{numero_elegido}.")
    else:
        print("Número de producto no válido.")
    
    mostrar_productos(lista_productos)
    
    opcion_iva = input("¿Desea ver los precios con IVA? (S/N): ")
    if opcion_iva.lower() == "s":
        mostrar_productos_iva(lista_productos, mostrar_iva=True)

    numero_elegido = int(input("Elija otro producto por su número para aplicar el descuento (0 para salir): "))

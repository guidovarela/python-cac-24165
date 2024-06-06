# Función para agregar productos a la lista
def agregar_producto(lista, numero_producto):
    descripcion = input(f"Ingrese la descripción del producto #{numero_producto}: ")
    precio = float(input("Ingrese el precio del producto: "))
    producto = {"descripcion": descripcion, "precio": precio}
    lista.append(producto)

# Función para definir productos al Cyber Monday
def aplicar_descuento_y_leyenda(producto):
    # aumento Cyber Monday - > 20% (ojo)
    producto["descripcion"] = "Cyber Monday: " + producto["descripcion"]
    producto["precio"] *= 0.85  # Aplicar un descuento del 15%

# Función para mostrar la lista de productos
def mostrar_productos(lista):
    if len(lista) == 0:
        print("La lista de productos está vacía.")
    else:
        print("Lista de productos:")
        for i, producto in enumerate(lista, 1):
            print(f"{i}. Descripción: {producto['descripcion']}, Precio: ${producto['precio']}")


# Función para mostrar la lista de productos
def mostrar_productos_iva(lista, mostrar_iva=False):
    if len(lista) == 0:
        print("La lista de productos está vacía.")
    else:
        print("Lista de productos:")
        for i, producto in enumerate(lista, 1):
            precio_con_iva = producto["precio"] * 1.21  # Aplicar un 21% de IVA
            if mostrar_iva:
                print(f"{i}. Descripción: {producto['descripcion']}, Precio: ${producto['precio']:.2f}, Precio con IVA: ${precio_con_iva:.2f}")
            else:
                print(f"{i}. Descripción: {producto['descripcion']}, Precio: ${producto['precio']:.2f}")

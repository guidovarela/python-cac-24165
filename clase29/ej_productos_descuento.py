from Productos import Producto

# Crear algunos productos
producto1 = Producto("Laptop", 1200, 10)
producto2 = Producto("Teléfono", 500, 20)
producto3 = Producto("Impresora", 200, 5)

# Mostrar información de los productos utilizando __str__
""" print(producto1)
print(producto2)
print(producto3)
 """
# Asignar productos a ventas con descuento
print(producto2)
# producto1.asignar_a_venta_con_descuento(0.1)  # Descuento del 10%
producto2.asignar_a_venta_con_descuento(0.2)  # Descuento del 20%
print(producto2)

# Mostrar información actualizada de los productos utilizando __str__
""" print(producto1)
print(producto2)
print(producto3) """

# Ejecutar una venta
print(producto1)
print("nueva venta!")
producto1.vender(5)
print(producto1)



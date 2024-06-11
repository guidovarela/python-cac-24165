class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # def mostrar_informacion(self):
    #     print(f"{self.nombre} - Precio: ${self.precio} - Stock disponible: {self.stock}")

    def vender(self, cantidad):
        if cantidad <= self.stock:
            print(f"Venta realizada: {cantidad} unidades de {self.nombre}")
            self.stock -= cantidad
        else:
            print(f"No hay suficiente stock disponible para vender {cantidad} unidades de {self.nombre}")

    def asignar_a_venta_con_descuento(self, descuento):
        if descuento > 0 and descuento <= 1:
            self.precio *= (1 - descuento)
            print(f"{self.nombre} asignado a una venta con descuento del {descuento * 100}%")
        else:
            print("El descuento debe estar en el rango de 0 a 1")

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Stock disponible: {self.stock}"
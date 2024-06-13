class Banco:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_cliente(self, nombre_cliente):
        for cliente in self.clientes:
            if cliente.nombre == nombre_cliente:
                return cliente
        return None

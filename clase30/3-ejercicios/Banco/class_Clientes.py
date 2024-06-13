class Cliente:
    def __init__(self, nombre, saldo_inicial=0):
        self._nombre = nombre
        self._saldo = saldo_inicial

    @property
    def nombre(self):
        return self._nombre

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            print("Error: No se permite un saldo negativo.")
        else:
            self._saldo = nuevo_saldo

    def realizar_deposito(self, monto):
        self._saldo += monto
        print("======================")
        print(f"Depósito de ${monto} realizado.")
        print(f"Nuevo saldo: ${self._saldo}")
        print("======================")

    def realizar_retiro(self, monto):
        if monto > self._saldo:
            print("Error: Fondos insuficientes.")
        else:
            self._saldo -= monto
            print("======================")
            print(f"Retiro de ${monto} realizado. Nuevo saldo: ${self._saldo}")
            print("======================")


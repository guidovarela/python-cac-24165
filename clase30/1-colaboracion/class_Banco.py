# from archivo import clase
from class_Cliente import Cliente

class Banco:
    def __init__(self):
       self.cliente1=Cliente("Marisa",1)
       self.cliente2=Cliente("Julian",2)
       self.cliente3=Cliente("Leo",3)

    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(1500)
        self.cliente3.depositar(2000)
        # self.cliente3.extraer(150)

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero en el banco es: {}".format(total))
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

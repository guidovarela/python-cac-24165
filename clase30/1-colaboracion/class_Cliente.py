class Cliente:
   def __init__(self,id,nombre):
       self.id=id
       self.nombre=nombre
       self.monto=0

   def depositar(self,monto):
       self.monto=self.monto+monto

   def extraer(self,monto):
       self.monto=self.monto-monto

   def retornar_monto(self):
       return self.monto

   def imprimir(self):
       print("----- Depositos -------")
    #    print("{} : ${}".format(self.nombre,self.monto))
       print(f"{self.nombre} : ${self.monto}")

       


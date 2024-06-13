class Cliente:
   suspendidos=[] #Atributo de Clase

   def __init__(self,codigo,nombre):
       self.codigo=codigo #Atributo de instancia
       self.nombre=nombre #Atributo de instancia

   def imprimir(self):
       print(f"Codigo: {self.codigo}")
       print(f"Nombre: {self.nombre}")
       self.esta_suspendido()

   def suspender(self):
        Cliente.suspendidos.append(self.codigo)
   def esta_suspendido(self):
           if self.codigo in Cliente.suspendidos:
               print("Esta suspendido")
           else:
               print("Esta habilitado")
           print("_"*20)

# Programa principal:
cliente1 = Cliente(1,"Juan")
cliente2 = Cliente(2,"Ana")
cliente3 = Cliente(3,"Diego")
cliente4 = Cliente(4,"Pedro")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()


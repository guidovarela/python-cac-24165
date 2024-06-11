
class Persona():
   def caminar(self): # Método caminar
       self.caminando = True # Atributo
       print("Estoy caminando.")

   def detener(self): # Método detener
       self.caminando = False
       print("Estoy detenido.")

juan = Persona() # Instanciamos -> objeto

""" juan.caminar()        # Estoy caminando
print(juan.caminando) # True
juan.detener()        # Estoy detenido
print(juan.caminando) # False """

class Cuadrado:
  def __init__(self, lado):
      self.lado = lado
  def calcular_perimetro(self):
      return self.lado * 4
  def calcular_area(self):
      return self.lado ** 2

figura1 =  Cuadrado(int(input("Cargar cantidad: ")))
print(figura1.calcular_area())



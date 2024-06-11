class Alumno: # Creamos la clase
  nro_alumnos = 0 # Cantidad de legajos existentes

  #Constructor
  def __init__(self,nombre,nota): 
    self.nombre = nombre
    self.nota = nota
    Alumno.nro_alumnos += 1 # Agregamos un legajo

  # Mostrar datos del objeto
  def __str__(self): 
    return f"Nombre: {self.nombre} (nota: {self.nota})"

  # Damos de baja el alumno
  def __del__(self): 
    Alumno.nro_alumnos -= 1 # Restamos un legajo
    print("Alumno dado de baja.")
    print(f"{Alumno.nro_alumnos} legajos restantes.")

  def mostrar_estado(self): # ¿está aprobado?
    print(f"El estado de {self.nombre} es ",end="" )
    if self.nota <= 4:
      print("regular")
    elif self.nota < 9:
      print("bueno")
    else:
      print("excelente")


# Programa principal
alumno1 = Alumno("Aldo López", 8)
alumno2 = Alumno("Juana Martín", 3)
print(alumno1) # Nombre: Aldo López (nota: 8) 
print(alumno2) # Nombre: Juana Martín (nota: 3)
alumno1.mostrar_estado() # El…de Aldo López es bueno
alumno2.mostrar_estado() # El…Juana Martín es regular
input("Pulse enter para salir")
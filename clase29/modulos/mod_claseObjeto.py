
# Clase Persona
class Persona:
    # atributos
    def __init__(self,nombre,apellido,edad,actividad):
        self.edad = edad
        self.apellido = apellido
        self.nombre = nombre
        self.actividad = actividad
    # metodos
    # def __str__(self):
    def saludar(self):
        return (f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años")

def cargarPersona(p):
    nombre = input("insertar Nombre:")
    apellido = input("insertar Apellido:")
    edad = int(input("insertar edad:"))
    nuevapersona = Persona(nombre,apellido,edad)
    p.append(nuevapersona)
    return True

def cargar_personas_xCantidad(p):
    cant = int(input("Cuantos usuarios vas a cargar? (0 para salir)"))
    if cant > 0:
        for i in range(cant):
            print(f"Usuario nro {i+1}:")
            cargarPersona(p)
            print(f"-------------")
        return p

def leerUsuarios(u):
    # print(personas)
    for i in range(len(u)):
        print(u[i])
        print("--------------")
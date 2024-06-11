
persona1_nombre = "Marisa"
persona2_nombre = "Julian"
persona1_edad = 23
persona2_edad = 45

"""
personas = [
    {
    "nombre":"Marisa",
    "edad":23
    },
]
"""

class Persona:
    # atributos
    # constructor
    # def indentificar(self,nombre,apellido,edad):
    def __init__(self,nombre,apellido,edad):
        self.edad = edad
        self.apellido = apellido
        self.nombre = nombre

    # metodos
    def __str__(self):
        return (f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años")

# instancia -> objeto
# persona1 = Persona("Marisa","Viotti",25)
# persona2 = Persona("Julian","Alvarez",21)
# print(persona1.saludar())
# print(persona2.saludar())
personas = []

def cargarPersona():
    nombre = input("insertar Nombre:")
    apellido = input("insertar Apellido:")
    edad = int(input("insertar Apellido:"))
    nuevapersona = Persona(nombre,apellido,edad)
    personas.append(nuevapersona)

def leerUsuarios(u):
    # print(personas)
    for i in range(len(u)):
        print(u[i].nombre)
        print(u[i].apellido)
        print(u[i].edad)
        print("--------------")

cargarPersona()
leerUsuarios(personas)
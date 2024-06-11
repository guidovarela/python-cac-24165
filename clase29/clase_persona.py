# Declarar una clase
class Persona:
    # metodos
    # def inicializar(self, n, e, a):
    #     self.nombre= n # Atributo
    #     self.edad= e
    #     self.apellido = a

    # Constructor - inicializador
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        # print("Hola, soy: " + self.nombre + " Edad: " + str(self.edad))
        return f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años"

    def __del__(self):
        return "objeto eliminado!"

    def caminar(self):
        print("Esta caminando")
    def parar(self):
        print(f"{self.nombre} esta detenida")

# Prog Ppal
# Instanciando la clase
persona1= Persona("Ramiro", "Perez", 40)
print(persona1)

persona2= Persona("Marcia", "Lopez", 23)
print(persona2)

# eliminar instancia
del persona2

persona2= Persona("Marcia", "Lopez", 23)
print(persona2)


""" persona2= Persona()
# print(persona1)
# print(persona2)
print(type(persona2))
texto= "Hola Mundo!"
print(type(texto)) # type me devuelve la clase del objeto

# Objeto que contiene un objeto
lista= [1, "Texto", 10.00, True] # Intancia de un objeto de tipo Lista
print(lista[1].upper())
 """
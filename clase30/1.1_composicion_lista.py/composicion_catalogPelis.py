class Pelicula:
   # Constructor de clase
   def __init__(self, titulo, duracion, lanzamiento):
       self.titulo = titulo
       self.duracion = duracion
       self.lanzamiento = lanzamiento
    #    print(f'Se ha creado la película: {self.titulo}')

   def __str__(self):
       return f'{self.titulo} ({self.lanzamiento})'
   
class Catalogo:
   peliculas = []
   # lista de objetos de la clase Pelicula  
   # Constructor de clase
   def __init__(self, peliculas):
       Catalogo.peliculas = peliculas

   def agregar(self, p): # p es un objeto Pelicula
       Catalogo.peliculas.append(p)

   def mostrar(self):
       for p in Catalogo.peliculas:
           print(p) # Print toma por defecto str(p)


# Instanciamos una película
peli1 = Pelicula("El Padrino", 175, 1972)

# Instanciamos un catálogo que contiene una pelicula
c = Catalogo([peli1])
c.mostrar()

# Añadimos una nueva película al catálogo:
c.agregar(peli1)
c.mostrar()

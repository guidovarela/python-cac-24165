""" Operadores de cadena
    Replicador *
    Concatenador +
    Comparación >, <, ==
    Longitud len()
    Métodos de las cadenas: upper(), lower(), capitalize(), split(), isdigit(), isalpha()
    Acceso a los elementos de una
    Rebanada
    Iterar una cadena

"""

cadena1 = "Cadena de caracteres"
cadena2 = 'Cadena de texto'
cadena3 = "456"

cadena = """Cadena de caracteres
sigue 
en la 
siguiente
 linea"""
cadena = '''Cadena de texto'''


# Replicador *
# Concatenador +
# Comparación >, <, ==

print(cadena2*3)
print(cadena+" Agregar más texto")
print(cadena2 > cadena3)
print(cadena2 < cadena3)
print(cadena2 == cadena3)

# Longitud len()
# cadena1 = "Cadena de caracteres"
longitud = len(cadena1)
print(longitud)


"""
Métodos de las cadenas: upper(), lower(), capitalize(), split(), isdigit(), isalpha()
Acceso a los elementos de una
Rebanada
Iterar una cadena
"""

texto = "ejemPlo de LOs Métodos De cadenAs"
print(texto.upper()) # Mayúsculas
print(texto.lower()) # Minúsculas

texto1 = "otro ejemplo para la letra capital"
print(texto1.capitalize())

# split()
nombre_completo = "Nina Polo"

nombre, apellido = nombre_completo.split(" ") # ["Nina", "Polo"]
print("Nombre", nombre)
print("Apellido", apellido)

# Contar cuántas palabras tiene texto3
texto3 = "Esto es una cadena de texto de ejemplo para calcular la longitud"

texto3_separado = texto3.split(" ")
print(len(texto3_separado))

# isdigit()
cadena4 = "96587"
print(cadena4.isdigit())


# isalpha()
cadena5 = "abcdario"
print(cadena5.isalpha())

cadena5 = "Es un string con las letras de abcdario"
cadena5_separada = cadena5.split(" ")

for palabra in cadena5_separada:
    print(palabra.isalpha())

cadena6 = "Manzana"
print(cadena6[0])
print(cadena6[2])
print(cadena6[len(cadena6)-1])
print(cadena6[-1])

# 012
# oso
# longitud: 3

# Rebanada
cadena7 = "Champiñones"
print(cadena7[0:4]) # 0 1 2 3 ojito 4 es limite
print(cadena7[:4])

# nes
print(cadena7[-3:])

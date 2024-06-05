cadena= '   Hola Mundo "Ramiro" más texto o 123 $%...'
print(cadena)
print(len(cadena))
print(cadena[8])
print(cadena[10]) # n
# cadena[10]= 'N' # TypeError: 'str' object does not support item assignment

# Buscar en una cadena
print(cadena.find('Hola')) # 3
print(cadena.find('Hola',10)) # -1

# iterar sobre cadena
for valor in cadena:
    print(valor)
print()

for valor in cadena:
    # if valor.isalpha():
    if not valor.isnumeric():
        print(valor)

# Reemplazar
print(cadena)
cadena= cadena.replace('Hola', '   HOLA   ')

# Más métodos de cadenas
print(cadena)
cadena= cadena.upper()
cadena= cadena.lower()
cadena= cadena.strip()
print(cadena)

# https://www.w3schools.com/python/python_ref_string.asp

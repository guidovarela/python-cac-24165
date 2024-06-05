"""
    Tuplas: son conjunto de elementos separados por  comas,
    encerrados entre paréntesis. Los paréntesis no son obligatorios. 
    Las tuplas son inmutables
    (elemento1, elemento2, elemento3)
    Acceso a los elementos: desempaquetando, por indice o rebanadas.
"""
# Dos formas de crear una tupla
tupla = ('uno', 'dos', 'tres')
tupla2 = "Enero", "Febrero", "Marzo"

m1, m2, m3 = tupla2

print(tupla[m3])
# print(tupla[1:])

for elemento in tupla2:
    print(elemento)



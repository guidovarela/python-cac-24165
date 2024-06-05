# Definir una lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Juan", "calificaciones": [5, 9, 8, 2, 8],"actividad":False},
    {"nombre": "María", "calificaciones": [6, 9, 2, 9, 9],"actividad":True},
    {"nombre": "Pedro", "calificaciones": [9, 8, 7, 8, 9],"actividad":False},
    {"nombre": "Ana", "calificaciones": [2, 9, 8, 9, 9],"actividad":True}
]


# Función para calcular el promedio de calificaciones de un estudiante
def calcular_promedio(calificaciones):
    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    return promedio

# Ciclo para calcular el promedio de cada estudiante y almacenarlo en un diccionario
promedios_estudiantes = {}
mejor_promedio = 0  # Inicializamos el mejor promedio con 0

for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    calificaciones = estudiante["calificaciones"]
    promedio = calcular_promedio(calificaciones)
    promedios_estudiantes[nombre] = promedio
    
    # Actualizamos el mejor promedio si encontramos uno mayor
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

# Imprimir los promedios de los estudiantes
for nombre, promedio in promedios_estudiantes.items():
    print(f"{nombre}: Promedio = {promedio}")

# Mostrar al estudiante con el mejor promedio
print(f"El estudiante con el mejor promedio es {mejor_estudiante} con un promedio de {mejor_promedio}")

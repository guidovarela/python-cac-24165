# Inicializamos variables para el número mayor, el número menor y la suma
numero_mayor = None
numero_menor = None
suma = 0
cantidad_numeros = 0  # Inicializamos el contador

while True:
    entrada = input("Ingresa un número (o 'fin' para terminar):")
    if entrada.lower() == 'fin':
        break

    try:
        numero = float(entrada)
        suma += numero
        cantidad_numeros += 1

        if numero_mayor is None or numero > numero_mayor:
            numero_mayor = numero

        if numero_menor is None or numero < numero_menor:
            numero_menor = numero
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número válido.")

if cantidad_numeros > 0:
    promedio = suma / cantidad_numeros
    print(f"Número mayor: {numero_mayor}")
    print(f"Número menor: {numero_menor}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron números.")

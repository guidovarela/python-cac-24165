while True:
    print("Ingrese operación a realizar:")
    print("1 Suma")
    print("2 Resta")
    operacion = str(input())

    if operacion == "1" or operacion == "2":
        print("¡Se termina el bucle!")
        break
    else:
        print("Palabra ingresada incorrecta, vuelva a intentar")

print(f"Operación a realizar: {operacion}")
numero_1 = int(input("Ingrese el primer número\n"))
numero_2 = int(input("Ingrese el segundo número\n"))

if operacion == "1":
    resultado = numero_1 + numero_2
elif operacion == "2":
    resultado = numero_1 - numero_2
else:
    print("Algo salio mal en el bucle...")

print(f"El resultado es: {resultado}")
print("FIN")
# Función para sumar dos números
def suma(x, y):
    return x + y

# Función para restar dos números
def resta(x, y):
    return x - y

# Función para multiplicar dos números
def multiplicacion(x, y):
    return x * y

# Función para dividir dos números
def division(x, y):
    if y == 0:
        return "Error: No se puede dividir por cero"
    return x / y

# Función principal
def calculadora():
    print("Calculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Elije una opción (1/2/3/4): ")
    
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    if opcion == '1':
        print("Resultado: ", suma(num1, num2))
    elif opcion == '2':
        print("Resultado: ", resta(num1, num2))
    elif opcion == '3':
        print("Resultado: ", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado: ", division(num1, num2))
    else:
        print("Opción no válida")

calculadora()

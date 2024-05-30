print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

cantOperaciones = 0

while True:
  print("CALCULADORA: Ingrese 2 numeros y luego seleccione la operacion a realizar: \n 1- SUMA \n 2- RESTA \n 3- MULTIPLICACION \n 4- DIVISION \n 5- SALIR. ")
  operacion = input("Seleccione una operacion: \n")
  numero_1 = float(input("Ingrese el primer numero: \n"))
  numero_2 = float(input("Ingrese el segundo numero: \n"))
  
  if operacion == "1":
    suma = numero_1 + numero_2
    resultado = suma
    cantOperaciones += 1
    print(resultado)

  elif operacion == "2":
    resta = numero_1 - numero_2
    resultado = resta
    cantOperaciones += 1
    print(resultado)
    
  elif operacion == "3":
    multiplicacion = numero_1 * numero_2
    resultado = multiplicacion
    cantOperaciones += 1
    print(resultado)
    
  elif operacion == "4":
    division = numero_1 / numero_2
    resultado = division
    cantOperaciones += 1
    print(resultado)
   
  elif operacion == "5":
    print("Gracias por utilizar la calculadorea de Python.")
    print(f"la calculadora funcionó {cantOperaciones} veces")
    break
  else:
    print("Error. Vuelva a intentarlo.")
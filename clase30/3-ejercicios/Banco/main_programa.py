from class_Banco import Banco
from class_Clientes import Cliente

banco = Banco()

num_clientes = int(input("Ingrese el número de clientes a cargar: "))

for _ in range(num_clientes):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    saldo_inicial = float(input("Ingrese el saldo inicial del cliente: "))

    cliente = Cliente(nombre_cliente, saldo_inicial)
    banco.agregar_cliente(cliente)

while True:
    print("\nOpciones:")
    print("1. Consultar saldo de un cliente")
    print("2. Consultar cantidad de clientes")
    print("3. Realizar un depósito")
    print("4. Realizar un retiro")
    print("0. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        nombre_buscar = input("Ingrese el nombre del cliente: ")
        cliente_encontrado = banco.buscar_cliente(nombre_buscar)
        if cliente_encontrado:
            print(f"Saldo de {nombre_buscar}: ${cliente_encontrado.saldo}")
        else:
            print(f"Cliente {nombre_buscar} no encontrado.")
    
    elif opcion == "2":
        print(f"Cantidad de clientes: {len(banco.clientes)}")
    
    elif opcion == "3":
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cliente = banco.buscar_cliente(nombre_cliente)
        if cliente:
            monto_deposito = float(input("Ingrese el monto a depositar: "))
            cliente.realizar_deposito(monto_deposito)
        else:
            print(f"Cliente {nombre_cliente} no encontrado.")
    
    elif opcion == "4":
        nombre_buscar = input("Ingrese el nombre del cliente: ")
        cliente = banco.buscar_cliente(nombre_cliente)
        if cliente:
            monto_retiro = float(input("Ingrese el monto a retirar: "))
            cliente.realizar_retiro(monto_retiro)
        else:
            print(f"Cliente {nombre_cliente} no encontrado.")

    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
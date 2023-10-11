def validacion_entrada(valor1, valor2, mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)

            if valor1 <= valor <= valor2:
                break
            else:
                print("\n=============================================")
                print("Error, debe ingresar un numero entre", valor1, "y", valor2, "!.")
                print("=============================================\n")
        else:
            print("\n========================================")
            print("Debes ingresar un valor numérico válido.")
            print("========================================\n")
    return valor


def validar_identificador(valor, mensaje="Ingrese un valor: "):
    while True:
        entrada = input(mensaje).replace(" ", "")
        if entrada.isdigit():
            val = str(entrada)
            tamanio = len(val)

            if tamanio >= valor:
                break
            else:
                print("\n==========================================================================")
                print("Error, debe ingresar un numero que sea igual o mayor a:", valor)
                print("==========================================================================\n")
        else:
            print("\n===========================================================")
            print("ATENCION! Debes ingresar un valor numérico válido (mayor o igual a:", valor)
            print("=============================================================\n")

    return val


def validar_patente(mensaje):
    while True:
        entrada = input(mensaje)
        entrada_mayusculas = entrada.upper()
        if len(entrada_mayusculas) > 0:
            break
        else:
            print("\n===========================================================")
            print("Debe ingresar una patente. Inténtalo nuevamente.")
            print("=============================================================\n")
    return entrada_mayusculas


def validacion_entrada(valor1, valor2, mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)

            if valor1 <= valor <= valor2:
                break
            else:
                print("\n=============================================")
                print("Error, debe ingresar un numero entre", valor1, "y", valor2, "!.")
                print("=============================================\n")
        else:
            print("\n========================================")
            print("Debes ingresar un valor numérico válido.")
            print("========================================\n")
    return valor

def validar_forma_pago(manual, telepeaje, mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)

            if valor == manual or valor == telepeaje:
                break
            else:
                print("\n==========================================================================================")
                print("Error, debe ingresar un numero entre", manual, "y", telepeaje, ". (1: manual, 2 telepeaje)!")
                print("==========================================================================================\n")
        else:
            print("\n========================================")
            print("Debes ingresar un valor numérico válido.")
            print("========================================\n")

    return valor
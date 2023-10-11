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

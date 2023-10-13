import os


def validacion_entrada(valor1, valor2, mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)

            if valor1 <= valor <= valor2:
                break
            else:
                print("\n"+"="*100)
                print("Error, debe ingresar un numero entre", valor1, "y", valor2, "!.")
                print("=" * 100)
        else:
            print("\n" + "=" * 100)
            print("Debes ingresar un valor numérico válido.")
            print("=" * 100)
    return valor


def validar_identificador(valor, mensaje="Ingrese un valor: "):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            val = int(entrada)

            if val >= valor:
                return val
            else:
                print("\n"+"="*100)
                print("Error, debe ingresar un numero que sea igual o mayor a:", valor)
                print("="*100)
        else:
            print("\n"+"="*100)
            print("ATENCION! Debe ingresar un valor numérico válido (mayor o igual a:", valor,").")
            print("="*100)


def validar_patente(mensaje):
    while True:
        entrada = input(mensaje)
        entrada_mayusculas = entrada.upper()

        if len(entrada_mayusculas) > 0:
            return entrada_mayusculas
        else:
            print("\n"+"="*100)
            print("Debe ingresar una patente. Inténtalo nuevamente.")
            print("="*100)


def validar_forma_pago(manual, telepeaje, mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)

            if valor == manual or valor == telepeaje:
                break
            else:
                print("\n"+"="*100)
                print("Error, debe ingresar un numero entre", manual, "y", telepeaje, ". (1: manual, 2 telepeaje)!")
                print("=" * 100)
        else:
            print("\n"+"="*100)
            print("Debes ingresar un valor numérico válido.")
            print("=" * 100)

    return valor


def existe_archivo_binario(fdb):
    if os.path.exists(fdb):
        return True
    return False

from funciones import *
from validaciones import *


def mostrar_menu():
    print("\n1.Crear archivo binario de registros")
    print("2.cargar por teclado los datos de un tiket")
    print("3.Mostrar todos los datos de todos los registros del archivo binario.")
    print("4.Mostrar todos los registros del archivo binario.")
    print("5.Buscarsi existe en el archivo binario un tiket cargado por teclado")
    print(
        "6.Determinar y mostrar la cantidad de vehiculos de cada combinacion posible entre tipo de vehiculo y pais de cabina en el archivo binario")
    print(
        "7. muestre la cantidad total de vehículos contados por cada tipo de vehículo posible, y la cantidad total de vehículos contados por cada país de cabina posible.")
    print(
        "8. Calcular y mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos del archivo binario")
    print("\ningrese 0 para finalizar\n")


def principal():
    documento = 'peajes-tp4.csv'
    documento_binario = 'ticket.dat'
    opcion = -1
    archivo_binario_cargado = False

    while opcion != 0:
        mostrar_menu()
        opcion = validacion_entrada(0, 9, "\ningrese una opcion: ")
        if int(opcion) == 1:
            if os.path.exists(documento_binario):
                while True:
                    entrada = int(input("esta seguro que desea eliminar el arreglo? (1 = Aceptar / 2 = Cancelar): "))
                    if entrada == 1 or entrada == 2:
                        if entrada == 1:
                            os.remove(documento_binario)
                            print(" Archivo binario eliminado existosamente.\n")
                            break
                        if entrada == 2:
                            break
                    else:
                        print("Debes ingresar un valor numérico válido entre(1 y 2).")
            else:
                cargar_datos_csv(documento, documento_binario)
                archivo_binario_cargado = True

        elif int(opcion) == 2 and archivo_binario_cargado:
            cargar_nuevo_ticket(documento_binario)


if __name__ == '__main__':
    principal()

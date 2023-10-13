from funciones import *
from validaciones import *


def mostrar_menu():
    print("\n" + "-" * 170)
    print("MENU PRINCIPAL:\n(Seleccione una opcion):")
    print("\n\t\t1. Crear archivo de registros.")
    print("\t\t2. Cargar por teclado los datos de un ticket.")
    print("\t\t3. Mostrar todos los datos de todos los registros del archivo.")
    print("\t\t4. Mostrar todos los registros del archivo binario de una patente que se cargue por teclado.")
    print("\t\t5. Buscar si existe en el archivo binario un codigo de ticket cargando el codigo por teclado.")
    print(
        "\t\t6. Determinar y mostrar la cantidad de vehiculos de cada combinacion posible entre tipo de vehiculo y pais de "
        "cabina.")
    print(
        "\t\t7. Mostrar la cantidad total de vehículos contados por cada tipo de vehículo posible, y la cantidad total de "
        "vehículos contados por cada país de cabina posible.")
    print(
        "\t\t8. Calcular y mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos del "
        "archivo binario")
    print("\n\t\t(Si desea finalizar presione: 0)\n")
    print("-" * 170)


def principal():
    documento = 'peajes-tp4.csv'
    documento_binario = 'ticket.dat'
    ingreso_al_punto_6 = ingreso_al_punto_7 = False
    opcion = -1
    matriz_contador = []

    while opcion != 0:
        mostrar_menu()
        opcion = validacion_entrada(0, 8, "\ningrese una opcion: ")
        if int(opcion) == 1:
            if existe_archivo_binario(documento_binario):
                while True:
                    entrada = int(input("\nEsta seguro que desea eliminar el arreglo? (1 = Aceptar / 2 = Cancelar): "))
                    if entrada == 1 or entrada == 2:
                        if entrada == 1:
                            os.remove(documento_binario)
                            print("\n" + "=" * 100)
                            print(" Archivo binario eliminado con exito.")
                            print("=" * 100)
                            break
                        if entrada == 2:
                            print("\n" + "=" * 100)
                            print("La operacion fue cancelada.")
                            print("=" * 100)
                            break
                    else:
                        print("\nATENCION! Debe ingresar un valor numérico válido entre(1 y 2).")
            else:
                cargar_datos_csv(documento, documento_binario)

        elif int(opcion) == 2 and existe_archivo_binario(documento_binario):
            cargar_nuevo_ticket(documento_binario)

        elif int(opcion) == 3 and existe_archivo_binario(documento_binario):
            mostrar_archivo(documento_binario)

        elif int(opcion) == 4 and existe_archivo_binario(documento_binario):
            buscar_patente(documento_binario)

        elif int(opcion) == 5 and existe_archivo_binario(documento_binario):
            buscar_codigo_ticket(documento_binario)

        elif int(opcion) == 6 and existe_archivo_binario(documento_binario):
            matriz_contador = matriz_cant_vehiculos(documento_binario)
            mostrar_matriz_contador(matriz_contador)
            ingreso_al_punto_6 = True

        elif int(opcion) == 7 and existe_archivo_binario(documento_binario):
            if ingreso_al_punto_6:
                cantidad_vehiculos(matriz_contador)
                ingreso_al_punto_7 = True
            else:
                print("-" * 105)
                print("ATENCION! Primero debe crear la matriz contador.(Ejecute el item anterior a éste y vuelva a "
                      "intentarlo.)")
                print("-" * 105)

        elif int(opcion) == 8 and existe_archivo_binario(documento_binario):
            if ingreso_al_punto_7:
                promedio = calcular_distancia_promedio(documento_binario)
                arreglor_registros = cargar_y_ordenar_registros(promedio, documento_binario)
                mostrar_promedio_y_arreglo_registros(promedio, arreglor_registros)
            else:
                print("-" * 100)
                print("ATENCION! Primero debe calcular el promedio de todas las distancias en km.(Ejecute el item "
                      "anterior a éste y vuelva a intentarlo.)")
                print("-" * 100)

        elif not existe_archivo_binario(documento_binario) and opcion != 0:
            print("\n"+"="*100)
            print("ATENCION! Primero debe crear el archivo de registros.")
            print("="*100)


if __name__ == '__main__':
    principal()

import pickle
from validaciones import *
import os
import io


class Ticket:
    def __init__(self, id, patent, tipo_de_vehiculo, forma_de_pago, pais_cabina, kilomentros, pais_vehiculo):
        self.id = id
        self.patente = patent
        self.tipo_vehiculo = tipo_de_vehiculo
        self.forma_pago = forma_de_pago
        self.pais_cabina = pais_cabina
        self.kilometros = kilomentros
        self.pais_vehiculo = pais_vehiculo

    def __str__(self):
        r = "Nro_Ticket:" + str(self.id) + "\t" + "Patente:" + str(self.patente) + "\t\t" + "Vehiculo:" + str(
            self.tipo_vehiculo) + "\t\t" + "Forma_pago:" + str(
            self.forma_pago) + "\t" + "Pais_cabina:" + str(self.pais_cabina) + "\t" + "Km:" + str(
            self.kilometros) + "\t" + "Pais de vehiculo:" + str(
            self.pais_vehiculo)
        return r


def cargar_datos_csv(fd, fdb):
    file = open(fd, "rt")
    file_binary = open(fdb, "wb")
    file.readline()
    file.readline()

    for line in file:
        line = line[:-1]
        ticket = line.split(",")
        id = ticket[0]
        patente = ticket[1]
        pais_vehiculo = pais_de_vehiculo(patente)
        tipo_vehiculo = ticket[2]
        forma_pago = ticket[3]
        pais_cabina = ticket[4]
        kilometros = ticket[5]

        registro = Ticket(id, patente, tipo_vehiculo, forma_pago, pais_cabina, kilometros, pais_vehiculo)

        pickle.dump(registro, file_binary)

    file.close()
    file_binary.close()
    print("\n"+"="*40)
    print("Archivo binario creado con exito.")
    print("="*40)


def pais_de_vehiculo(patentee):
    if len(patentee) == 7:
        if patentee[0:2].isalpha() and patentee[2:5].isdigit() and patentee[5:7].isalpha():
            # argentina AA333AA
            procedencia_vehiculo = "Argentina"

        elif patentee[0:3].isalpha() and patentee[3].isdigit() and patentee[4].isalpha() and patentee[5:7].isdigit():
            # brasil
            procedencia_vehiculo = "Brasil"
        elif patentee[0] == " " and patentee[1:5].isalpha() and patentee[5:7].isdigit():
            # chile
            procedencia_vehiculo = "Chile"
        elif patentee[0:2].isalpha() and patentee[2:].isdigit():
            # Bolivia
            procedencia_vehiculo = "Bolivia"
        elif patentee[0:4].isalpha() and patentee[4:].isdigit():
            # paraguay
            procedencia_vehiculo = "Paraguay"
        elif patentee[0:3].isalpha() and patentee[3:].isdigit():
            # uruguay
            procedencia_vehiculo = "Uruguay"
        else:
            # otro
            procedencia_vehiculo = "Otro"
    else:
        # Otro
        procedencia_vehiculo = "Otro"

    return procedencia_vehiculo


def mostrar_archivo(fdb):
    print("Contenido actual del achivo", fdb, ":")
    file_binary = open(fdb, "rb")

    # registros almacenados uno a uno en forma secuencial...
    t = os.path.getsize(fdb)
    while file_binary.tell() < t:
        ticket = pickle.load(file_binary)
        print(ticket)
    file_binary.close()
    print()


def buscar_patente(fdb):
    patente_validada = validar_patente("Ingrese una patente para buscar en el sistema:")
    contador_registros_mostrados = 0

    file_binary = open(fdb, "rb")

    t = os.path.getsize(fdb)
    print()
    while file_binary.tell() < t:
        ticket = pickle.load(file_binary)
        if ticket.patente == patente_validada:
            print(ticket)
            contador_registros_mostrados += 1

    if contador_registros_mostrados == 0:
        print("No se encontraron patentes.")

    print("\ncantidad de registros mostrados:", contador_registros_mostrados)
    file_binary.close()
    print()


def buscar_codigo_ticket(fdb):
    id_validado = validar_identificador(1, "Ingrese codigo de ticket a buscar en el sistema:")
    se_encontro_id = False
    file_binary = open(fdb, "rb")
    t = os.path.getsize(fdb)
    print()
    while file_binary.tell() < t:
        ticket = pickle.load(file_binary)
        if ticket.id == id_validado:
            print(ticket)
            se_encontro_id = True
            break
    if not se_encontro_id:
        print("\n No se encontró codigo de ticket.")

    file_binary.close()
    print()


def calcular_distancia_promedio(fdb):
    file_binary = open(fdb, "rb")
    t = os.path.getsize(fdb)
    acumulador_km = 0
    acumulador_cantidad = 0

    while file_binary.tell() < t:
        ticket = pickle.load(file_binary)
        acumulador_km += int(ticket.kilometros)
        acumulador_cantidad += 1

    if acumulador_cantidad != 0:
        promedio = acumulador_km // acumulador_cantidad
        return promedio
    else:
        return 0


def matriz_cant_vehiculos(fdb):
    mat = [[0] * 3 for _ in range(5)]

    file_binary = open(fdb, "rb")
    t = os.path.getsize(fdb)
    while file_binary.tell() < t:
        ticket = pickle.load(file_binary)
        col = int(ticket.tipo_vehiculo)
        fil = int(ticket.pais_cabina)
        mat[fil][col] += 1

    file_binary.close()
    return mat


def mostrar_matriz_contador(mat):
    pais_cabina = ["Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay"]
    tipo_vehiculo = ["moto", "auto", "camion"]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            resp_cant = "Para el tipo de vehiculo:" + tipo_vehiculo[j] + \
                        "\t\ty para el pais de cabina:" + pais_cabina[i] + \
                        "\t\thay un total de:" + str(mat[i][j]) + " vehículos."

            print(resp_cant)


def cantidad_vehiculos(mat):
    vehiculos = ["motos", "autos", "camiones"]
    pais_cabina = ["Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay"]
    cont_por_tipo_vehiculo = [0] * 3
    cont_por_cada_cabina = [0] * 5

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            cont_por_tipo_vehiculo[j] += mat[i][j]
            cont_por_cada_cabina[i] += mat[i][j]
    print()
    print("Cantidad total por tipo de vehiculo:")
    for i in range(len(cont_por_tipo_vehiculo)):
        print("La cantidad total de:", vehiculos[i], "por cada tipo de vehiculo posible es:", cont_por_tipo_vehiculo[i])
    print()
    print("Cantidad total por pais de cabina:")
    for i in range(len(cont_por_cada_cabina)):
        print("La cantidad total de vehiculos por cabina de:", pais_cabina[i], "es:", cont_por_cada_cabina[i])


def cargar_nuevo_ticket(fdb):
    file_binary = open(fdb, "ab")

    id = validar_identificador(1, mensaje="\nIngrese identificador (debe ser mayor o igual a 1): ")
    patente = validar_patente(mensaje="\nIngrese patente (puede contener cualquier tamaño): ")
    tipo_vehiculo = validacion_entrada(0, 2,
                                       mensaje="\nIngrese el tipo de vehiculo: (0: motocicleta,1: automóvil,"
                                               "2: camión): ")
    forma_pago = validar_forma_pago(1, 2, mensaje="\ningrese la forma de pago (1: manual, 2 telepeaje): ")
    pais_cabina = validacion_entrada(0, 4, mensaje="\nIngrese donde se encuentra la cabina (0: "
                                                   "Argentina - 1: Bolivia - 2: Brasil - 3: "
                                                   "Paraguay - 4: Uruguay): ")
    kilometros = validacion_entrada(0, 999, mensaje="\nIngrese la distancia en Km entre (0 y 999): ")
    pais_vehiculo = pais_de_vehiculo(patente)

    registro = Ticket(id, patente, tipo_vehiculo, forma_pago, pais_cabina, kilometros, pais_vehiculo)

    pickle.dump(registro, file_binary)
    file_binary.close()

    print("\nSe cargo correctamente el archivo binario\n")


def ordenamiento_shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1

    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and int(y.kilometros) < int(v[k].kilometros):
                v[k + h] = v[k]
                k -= h
            v[k + h] = y
        h //= 3


def cargar_y_ordenar_registros(prom, fdb):
    arreglo_registros = []
    file_binary = open(fdb, 'rb')
    t = os.path.getsize(fdb)
    """
    Leemos archivo binario sesde la posicion 0: file_binary.seek(0, io.SEEK_SET)
    """
    file_binary.seek(0, io.SEEK_SET)
    while file_binary.tell() < t:
        ticket = pickle.load(file_binary)
        if int(ticket.kilometros) > int(prom):
            arreglo_registros.append(ticket)

    file_binary.close()

    ordenamiento_shell_sort(arreglo_registros)

    return arreglo_registros


def mostrar_promedio_y_arreglo_registros(prom, vec):
    print("El promedio es:", prom)
    for i in range(len(vec)):
        print(vec[i])

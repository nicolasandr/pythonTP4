import pickle
from validaciones import *
import os


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
    print("Archivo binario creado exitosamente")


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


def buscar_codigo_ticket(fdb):
    id_validado = validar_identificador(1, "Ingrese codigo de ticket a buscar en el sistema:")
    file_binary = open(fdb, "rb")
    se_encontro_id = False

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

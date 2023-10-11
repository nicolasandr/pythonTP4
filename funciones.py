import pickle
from validaciones import *
import os


class Ticket:
    def __init__(self, id, patent, tipo_de_vehiculo, forma_de_pago, pais_cabina, kilomentros):
        self.id = id
        self.patente = patent
        self.tipo_vehiculo = tipo_de_vehiculo
        self.forma_pago = forma_de_pago
        self.pais_cabina = pais_cabina
        self.kilometros = kilomentros

    def __str__(self):
        r = "Nro_Ticket:" + str(self.id) + "\t" + "Patente:" + str(self.patente) + "\t\t" + "Vehiculo:" + str(
            self.tipo_vehiculo) + "\t\t" + "Forma_pago:" + str(
            self.forma_pago) + "\t" + "Pais_cabina:" + str(self.pais_cabina) + "\t" + "Km:" + str(self.kilometros)
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
        tipo_vehiculo = ticket[2]
        forma_pago = ticket[3]
        pais_cabina = ticket[4]
        kilometros = ticket[5]

        registro = Ticket(id, patente, tipo_vehiculo, forma_pago, pais_cabina, kilometros)

        pickle.dump(registro, file_binary)

    file.close()
    file_binary.close()
    print("Archivo binario creado exitosamente")

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

    registro = Ticket(id, patente, tipo_vehiculo, forma_pago, pais_cabina, kilometros)

    pickle.dump(registro, file_binary)
    file_binary.close()

    print("\nSe cargo correctamente el archivo binario\n")

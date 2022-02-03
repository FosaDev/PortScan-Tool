import socket
import sys


def RevisionDePuertos(ip, ListaDePuertos):
    try:
        for Puertos in ListaDePuertos:
            Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)
            Socket.settimeout(5)
            Resultado = Socket.connect_ex((ip, Puertos))
            if Resultado == 0:
                print("Puerto {}: \t Abierto".format(Puertos))
            Socket.close()
    except Socket.error as error:
        print(str(error))
        print("La conexion a fallado")
        sys.exit()

DireccionIp = input("Digite la direccion Ip: ")
for i in range(65535):
    i += 1
    RevisionDePuertos(DireccionIp, [i])
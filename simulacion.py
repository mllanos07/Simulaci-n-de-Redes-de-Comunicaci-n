class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def AgregaCconexion(self, nodo):
        self.conexiones.append(nodo)

    def EnviarMensaje(self, mensaje):
        print(f"{self.nombre} envía mensaje: {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje, self.nombre)

    def RecibirMensaje(self, mensaje, remitente):
        print(f"{self.nombre} recibió mensaje de {remitente}: {mensaje}")

servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente1")
cliente2 = Nodo("Cliente2")
cliente3 = Nodo("Cliente3")

servidor.AgregaCconexion(cliente1)
servidor.AgregaCconexion(cliente2)
servidor.AgregaCconexion(cliente3)

envio = "Hola, clientes!"
servidor.EnviarMensaje(envio)

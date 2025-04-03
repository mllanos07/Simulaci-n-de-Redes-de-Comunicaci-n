Simulación de Red en Python

Descripción:

Este proyecto es una simulación básica de una red de comunicación en Python utilizando Programación Orientada a Objetos (POO). El objetivo es representar la interacción entre un servidor y tres clientes, permitiendo que el servidor envíe mensajes a los clientes conectados.

Estructura del Código

    El código implementa una clase Nodo que representa un dispositivo en la red.
    Cada Nodo puede conectarse con otros nodos y enviarles mensajes.

Clase Nodo

Atributos:

    -nombre: Nombre del nodo (Ejemplo: "Servidor" o "Cliente1").

    -conexiones: Lista de nodos conectados a este nodo.

Métodos:

1-__init__(self, nombre): Constructor que inicializa el nodo con un nombre y una lista vacía de conexiones.

2-AgregaCconexion(self, nodo): Agrega otro nodo a la lista de conexiones.

3-EnviarMensaje(self, mensaje): Envía un mensaje a todos los nodos conectados.

4-RecibirMensaje(self, mensaje, remitente): Recibe un mensaje y muestra quién lo envió.

Uso

1-Se crean cuatro nodos:

    Un servidor

    Tres clientes

2-Se establecen conexiones entre el servidor y los clientes usando AgregaCconexion().

3-El servidor envía un mensaje a todos los clientes usando EnviarMensaje().
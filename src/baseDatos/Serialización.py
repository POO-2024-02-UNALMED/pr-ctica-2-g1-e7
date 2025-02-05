import Serialización

class BaseDatos:
    def __init__(self):
        self.__datos = []
        self.__serialización = Serialización.Serialización()

    def agregar(self, dato):
        self.__datos.append(dato)

    def guardar(self, archivo):
        self.__serialización.guardar(archivo, self.__datos)

    def cargar(self, archivo):
        self.__datos = self.__serialización.cargar(archivo)

    def __str__(self):
        return str(self.__datos)

from enum import Enum

class TipoTransporte(Enum):
    CAMION = (15000, 16329, "Camion")
    AVION = (30000, 64000, "Avion")
    AUTOMOVIL = (9000, 500, "Automovil")
    CAMIONETA = (12000, 650, "Camioneta")
    BICICLETA = (5000, 35, "Bicicleta")
    PATINES = (3000, 20, "Patines")
    BARCO = (20000, 3356835, "Barco")
    HELICOPTERO = (70000, 29000, "Helicoptero")
    TREN = (20000, 30000, "Tren")
    CAMINANDO = (5000, 15, "Caminando")

    def __init__(self, precioEnvio, capacidadMax, nombre):
        self.precioEnvio = precioEnvio
        self.capacidadMax = capacidadMax
        self.nombre = nombre

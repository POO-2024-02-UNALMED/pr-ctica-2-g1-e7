
from Persona import Persona

class Conductor(Persona):
    listaConductores = []  # Lista de todos los conductores

    def __init__(self, nombre=None, cedula=None, edad=None, cuentaBancaria=None, fabrica=None, transporte=None, licencia=None):
        if (nombre is not None and cedula is not None and edad is not None and
                cuentaBancaria is not None and fabrica is not None and transporte is not None):
            super().__init__(nombre, cedula, edad, cuentaBancaria)
            self.transporte = transporte
            # Se asume que el objeto 'transporte' posee el método setConductor
            transporte.setConductor(self)
            self.fabrica = fabrica
            self.metaConductor = []
            Conductor.listaConductores.append(self)
            self.licencia = licencia  # Puede ser None si no se pasó
        else:
            # Constructor vacío
            pass

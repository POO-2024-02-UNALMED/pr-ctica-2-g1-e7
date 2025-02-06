from Persona import Persona

class Operario(Persona):
    listaOperario = []  # Lista de todos los operarios

    def __init__(self, nombre=None, cedula=None, edad=None, cuentaBancaria=None, fabrica=None):
        if (nombre is not None and cedula is not None and edad is not None and
                cuentaBancaria is not None and fabrica is not None):
            super().__init__(nombre, cedula, edad, cuentaBancaria)
            self.fabrica = fabrica
            self.metaOperario = []
            Operario.listaOperario.append(self)
        else:
            # Constructor vacío
            pass

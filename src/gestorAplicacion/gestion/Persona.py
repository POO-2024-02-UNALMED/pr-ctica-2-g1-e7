
from abc import ABC

class Persona(ABC):
    SALARIOBASE = 10000      # Constante de clase (salario base)
    personasTotales = 0      # Contador de todas las personas creadas
    listaPersonas = []       # Lista de todas las instancias de Persona

    def __init__(self, nombre=None, cedula=None, edad=None, cuentaBancaria=None):
        if nombre is not None and cedula is not None and edad is not None and cuentaBancaria is not None:
            self.nombre = nombre
            self.cedula = cedula
            self.edad = edad
            self.cuentaBancaria = cuentaBancaria
            self.cantidadTrabajo = 0
            self.indiceMeta = 0
            Persona.personasTotales += 1
            Persona.listaPersonas.append(self)
        else:
            # Constructor vacío
            pass

from abc import ABC, abstractmethod

class Persona(ABC):
    SALARIO_BASE = 10000  # Salario base que después se modifica por cantidad de veces trabajadas y por bonos
    personasTotales = 0
    listaPersonas = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuentaBancaria):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.cuentaBancaria = cuentaBancaria
        self.cantidadTrabajo = 0
        self.indiceMeta = 0
        
        Persona.personasTotales += 1
        Persona.listaPersonas.append(self)
    
    @abstractmethod
    def recibirSueldo(self, valor: float):
        pass
    
    @abstractmethod
    def mostrarMetas(self) -> str:
        pass
    
    @abstractmethod
    def getMeta(self):
        pass
    
    # Getters y Setters
    def getNombre(self) -> str:
        return self.nombre
    
    def setNombre(self, nombre: str):
        self.nombre = nombre
    
    def getCedula(self) -> int:
        return self.cedula
    
    def setCedula(self, cedula: int):
        self.cedula = cedula
    
    def getEdad(self) -> int:
        return self.edad
    
    def setEdad(self, edad: int):
        self.edad = edad
    
    def getCantidadTrabajo(self) -> int:
        return self.cantidadTrabajo
    
    def setCantidadTrabajo(self, cantidadTrabajo: int):
        self.cantidadTrabajo = cantidadTrabajo
    
    def getCuentaBancaria(self):
        return self.cuentaBancaria
    
    def setCuentaBancaria(self, cuentaBancaria):
        self.cuentaBancaria = cuentaBancaria
    
    @classmethod
    def getSalarioBase(cls) -> int:
        return cls.SALARIO_BASE
    
    def getIndiceMeta(self) -> float:
        return self.indiceMeta
    
    def setIndiceMeta(self, indiceMeta: float):
        self.indiceMeta = indiceMeta
    
    @classmethod
    def getPersonasTotales(cls) -> int:
        return cls.personasTotales
    
    @classmethod
    def getListaPersonas(cls):
        return cls.listaPersonas

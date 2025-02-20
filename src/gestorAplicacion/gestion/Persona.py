from abc import ABC, abstractmethod

class Persona(ABC):
    SALARIO_BASE = 10000  # Salario base que después se modifica por cantidad de veces trabajadas y por bonos
    personasTotales = 0
    listaPersonas = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuenta_bancaria):
        self._nombre = nombre
        self._cedula = cedula
        self._edad = edad
        self._cuentaBancaria = cuenta_bancaria
        self._cantidadTrabajo = 0
        self._indiceMeta = 0
        
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
        return self._nombre
    
    def setNombre(self, nombre: str):
        self._nombre = nombre
    
    def getCedula(self) -> int:
        return self._cedula
    
    def setCedula(self, cedula: int):
        self._cedula = cedula
    
    def getEdad(self) -> int:
        return self._edad
    
    def setEdad(self, edad: int):
        self._edad = edad
    
    def getCantidadTrabajo(self) -> int:
        return self._cantidadTrabajo
    
    def setCantidadTrabajo(self, cantidad_trabajo: int):
        self._cantidadTrabajo = cantidad_trabajo
    
    def getCuentaBancaria(self):
        return self._cuentaBancaria
    
    def setCuentaBancaria(self, cuenta_bancaria):
        self._cuentaBancaria = cuenta_bancaria
    
    @classmethod
    def getSalarioBase(cls) -> int:
        return cls.SALARIO_BASE
    
    def getIndiceMeta(self) -> float:
        return self._indiceMeta
    
    def setIndiceMeta(self, indice_meta: float):
        self.indice_meta = indice_meta
    
    @classmethod
    def getPersonasTotales(cls) -> int:
        return cls.personasTotales
    
    @classmethod
    def getListaPersonas(cls):
        return cls.listaPersonas

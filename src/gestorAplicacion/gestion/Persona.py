from abc import ABC, abstractmethod

class Persona(ABC):
    SALARIO_BASE = 10000  # Salario base que después se modifica por cantidad de veces trabajadas y por bonos
    personasTotales = 0
    listaPersonas = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuenta_bancaria):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad
        self.__cuentaBancaria = cuenta_bancaria
        self.__cantidadTrabajo = 0
        self.__indiceMeta = 0
        
        Persona.personas_totales += 1
        Persona.lista_personas.append(self)
    
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
        return self.__nombre
    
    def setNombre(self, nombre: str):
        self.__nombre = nombre
    
    def getCedula(self) -> int:
        return self.__cedula
    
    def setCedula(self, cedula: int):
        self.__cedula = cedula
    
    def getEdad(self) -> int:
        return self.__edad
    
    def setEdad(self, edad: int):
        self.__edad = edad
    
    def getCantidadTrabajo(self) -> int:
        return self.__cantidadTrabajo
    
    def setCantidadTrabajo(self, cantidad_trabajo: int):
        self.__cantidadTrabajo = cantidad_trabajo
    
    def getCuentaBancaria(self):
        return self.__cuentaBancaria
    
    def setCuentaBancaria(self, cuenta_bancaria):
        self.__cuentaBancaria = cuenta_bancaria
    
    @classmethod
    def getSalarioBase(cls) -> int:
        return cls.SALARIO_BASE
    
    def getIndiceMeta(self) -> float:
        return self.__indiceMeta
    
    def setIndiceMeta(self, indice_meta: float):
        self.indice_meta = indice_meta
    
    @classmethod
    def getPersonasTotales(cls) -> int:
        return cls.personasTotales
    
    @classmethod
    def getListaPersonas(cls):
        return cls.listaPersonas

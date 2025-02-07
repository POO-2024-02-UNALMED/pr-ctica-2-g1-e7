from abc import ABC, abstractmethod

class Persona(ABC):
    SALARIO_BASE = 10000  # Salario base que después se modifica por cantidad de veces trabajadas y por bonos
    personas_totales = 0
    lista_personas = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuenta_bancaria):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.cuenta_bancaria = cuenta_bancaria
        self.cantidad_trabajo = 0
        self.indice_meta = 0
        
        Persona.personas_totales += 1
        Persona.lista_personas.append(self)
    
    @abstractmethod
    def recibir_sueldo(self, valor: float):
        pass
    
    @abstractmethod
    def mostrar_metas(self) -> str:
        pass
    
    @abstractmethod
    def get_meta(self):
        pass
    
    # Getters y Setters
    def get_nombre(self) -> str:
        return self.nombre
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def get_cedula(self) -> int:
        return self.cedula
    
    def set_cedula(self, cedula: int):
        self.cedula = cedula
    
    def get_edad(self) -> int:
        return self.edad
    
    def set_edad(self, edad: int):
        self.edad = edad
    
    def get_cantidad_trabajo(self) -> int:
        return self.cantidad_trabajo
    
    def set_cantidad_trabajo(self, cantidad_trabajo: int):
        self.cantidad_trabajo = cantidad_trabajo
    
    def get_cuenta_bancaria(self):
        return self.cuenta_bancaria
    
    def set_cuenta_bancaria(self, cuenta_bancaria):
        self.cuenta_bancaria = cuenta_bancaria
    
    @classmethod
    def get_salario_base(cls) -> int:
        return cls.SALARIO_BASE
    
    def get_indice_meta(self) -> float:
        return self.indice_meta
    
    def set_indice_meta(self, indice_meta: float):
        self.indice_meta = indice_meta
    
    @classmethod
    def get_personas_totales(cls) -> int:
        return cls.personas_totales
    
    @classmethod
    def get_lista_personas(cls):
        return cls.lista_personas

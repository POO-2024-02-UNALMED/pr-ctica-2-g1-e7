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

class Vendedor(Persona):
    listaVendedores = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuentaBancaria):
        super().__init__(nombre, cedula, edad, cuentaBancaria)
        self.tienda = None
        self.metaVendedor = []
        Vendedor.listaVendedores.append(self)
    
    def mostrarMetas(self) -> str:
        texto = []
        metas_no_verificadas = [meta for meta in self.metaVendedor if not meta.getVerificador()] 

        for idx, meta in enumerate(metas_no_verificadas, start=1): 
            texto.append(f"\nMeta {idx}: {meta}")  
        return "".join(texto)  
    
    def __str__(self) -> str:
        return (f"\nNombre: {self.getNombre()}\n"
                f"Cedula: {self.getCedula()}\n"
                f"Edad: {self.getEdad()}\n"
                f"Tienda: {self.tienda.getNombre() if self.tienda else 'No asignada'}")
    
    def recibirSueldo(self, valor: float):
        self.getCuentaBancaria().añadirDinero(valor)
        self.setCantidadTrabajo(0)
    
    def setTienda(self, tienda):
        self.tienda = tienda
    
    def getTienda(self):
        return self.tienda
    
    def getMeta(self):
        return self.metaVendedor
    
    def setMetaVendedor(self, meta):
        self.metaVendedor.append(meta)
    
    @classmethod
    def getListaVendedores(cls):
        return cls.listaVendedores
    
    def aumentarCargaTrabajo(self):
        self.cantidadTrabajo += 1
    
    def aumentarIndiceMeta(self):
        self.setIndiceMeta(self.getIndiceMeta() + 1)

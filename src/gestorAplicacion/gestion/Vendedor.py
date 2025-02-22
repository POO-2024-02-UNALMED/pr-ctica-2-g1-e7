import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from gestorAplicacion.gestion.Persona import Persona

class Vendedor(Persona):
    listaVendedores = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuentaBancaria):
        super().__init__(nombre, cedula, edad, cuentaBancaria)
        self._tienda = None
        self._metaVendedor = []
        Vendedor.listaVendedores.append(self)
    
    def mostrarMetas(self) -> str:
        texto = []
        metasNoVerificadas = [meta for meta in self._metaVendedor if not meta.getVerificador()] 

        for idx, meta in enumerate(metasNoVerificadas, start=1): 
            texto.append(f"\nMeta {idx}: {meta}")  
        return "".join(texto)  
    
    def __str__(self) -> str:
        return (f"\nNombre: {self.getNombre()}\n"
                f"Cedula: {self.getCedula()}\n"
                f"Edad: {self.getEdad()}\n"
                f"Tienda: {self.tienda.getNombre() if self._tienda else 'No asignada'}")
    
    def recibirSueldo(self, valor: float):
        self.getCuentaBancaria().añadirDinero(valor)
        self.setCantidadTrabajo(0)
    
    def setTienda(self, tienda):
        self._tienda = tienda
    
    def getTienda(self):
        return self._tienda
    
    def getMeta(self):
        return self._metaVendedor
    
    def setMetaVendedor(self, meta):
        self._metaVendedor.append(meta)
    
    @classmethod
    def getListaVendedores(cls):
        return cls.listaVendedores
    
    def aumentarCargaTrabajo(self):
        self._cantidadTrabajo += 1
    
    def aumentarIndiceMeta(self):
        self.setIndiceMeta(self.getIndiceMeta() + 1)

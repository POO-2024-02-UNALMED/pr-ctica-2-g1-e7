import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from gestorAplicacion.gestion.Persona import Persona

class Conductor(Persona):
    listaConductores = []
    def __init__(self, nombre: str, cedula: int, edad: int, cuentaBancaria, fabrica, transporte, licencia: str = None):
        from gestorAplicacion.produccion.Transporte import Transporte
        super().__init__(nombre, cedula, edad, cuentaBancaria)
        self._transporte: Transporte = transporte
        self._fabrica = fabrica
        self._metaConductor = []
        self._licencia = licencia
        transporte.setConductor(self)
        Conductor.listaConductores.append(self)
    
    def mostrarMetas(self) -> str:
        texto = []
        metaSNoVerificadas = [meta for meta in self._metaConductor if not meta.getVerificador()] 

        for idx, meta in enumerate(metaSNoVerificadas, start=1): 
            texto.append(f"\nMeta {idx}: {meta}")  
        return "".join(texto)  
    
    def __str__(self) -> str:
        return (f"\nNombre: {self.getNombre()}\n"
                f"Cedula: {self.getCedula()}\n"
                f"Edad: {self.getEdad()}\n"
                f"Transporte: {self.transporte.getTipoTransporte()}")
    
    def recibirSueldo(self, valor: float):
        self.getCuentaBancaria().añadirDinero(valor)
        self.setCantidadTrabajo(0)
    
    def getTransporte(self):
        return self._transporte
    
    def setTransporte(self, transporte):
        self._transporte = transporte

    def getFabrica(self):
        return self._fabrica
    
    def setFabrica(self, fabrica):
        self._fabrica = fabrica
    
    @classmethod
    def getListaConductores(cls):
        return cls.listaConductores
    
    def getMeta(self):
        return self._metaConductor
    
    def setMetaConductor(self, meta):
        self._metaConductor.append(meta)
    
    def aumentarCargaTrabajo(self):
        self._cantidadTrabajo += 1
    
    def aumentarIndiceMeta(self, peso: float):
        self.setIndiceMeta(self.getIndiceMeta() + peso)
    
    def getLicencia(self) -> str:
        return self._licencia
    
    def setLicencia(self, licencia: str):
        self._licencia = licencia



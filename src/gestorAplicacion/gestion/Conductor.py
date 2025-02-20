from gestorAplicacion.gestion.Persona import Persona
from gestorAplicacion.produccion.Transporte import Transporte
from gestorAplicacion.produccion.TipoTransporte import TipoTransporte

class Conductor(Persona):
    listaConductores = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuentaBancaria, fabrica, transporte, licencia: str = None):
        #from produccion.Transporte import Transporte
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
        self.getCuentaBancaria().anadirDinero(valor)
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
transporte1 = Transporte(TipoTransporte.CAMION, 16000, 15000)
transporte2 = Transporte(TipoTransporte.AVION, 60000, 30000)
transporte3 = Transporte(TipoTransporte.BICICLETA, 30, 5000)
transporte4 = Transporte(TipoTransporte.PATINES, 15, 3000)
transporte5 = Transporte(TipoTransporte.BARCO, 100000, 20000)
transporte6 = Transporte(TipoTransporte.HELICOPTERO, 5000, 70000)
transporte7 = Transporte(TipoTransporte.TREN, 50000, 20000)
transporte8 = Transporte(TipoTransporte.AUTOMOVIL, 400, 9000)
transporte9 = Transporte(TipoTransporte.CAMIONETA, 600, 12000)

# Crear conductores individualmente y asignarlos a transportes
conductor1 = Conductor("Juan Pérez", 12345678, 35, "123-456-789", "Fábrica X", transporte1, "Licencia A")
conductor2 = Conductor("María Gómez", 87654321, 40, "987-654-321", "Fábrica Y", transporte2, "Licencia B")
conductor3 = Conductor("Carlos Rodríguez", 11223344, 29, "112-233-445", "Fábrica Z", transporte3, "Licencia C")
conductor4 = Conductor("Laura Sánchez", 55667788, 33, "556-677-889", "Fábrica W", transporte4, "Licencia D")
conductor5 = Conductor("Andrés Ramírez", 99887766, 45, "998-877-665", "Fábrica V", transporte5, "Licencia E")
conductor6 = Conductor("Sofía Herrera", 33445566, 38, "334-455-667", "Fábrica U", transporte6, "Licencia F")
conductor7 = Conductor("Ricardo Torres", 77889900, 42, "778-899-001", "Fábrica T", transporte7, "Licencia G")
conductor8 = Conductor("Valeria Martínez", 44332211, 31, "443-322-110", "Fábrica S", transporte8, "Licencia H")
conductor9 = Conductor("Gabriel Castillo", 66554433, 27, "665-544-332", "Fábrica R", transporte9, "Licencia I")
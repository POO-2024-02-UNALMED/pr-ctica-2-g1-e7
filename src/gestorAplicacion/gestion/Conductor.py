from gestorAplicacion.gestion.Persona import Persona
class Conductor(Persona):
    listaConductores = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuentaBancaria, fabrica, transporte, licencia: str = None):
        from produccion.Transporte import Transporte
        super().__init__(nombre, cedula, edad, cuentaBancaria)
        self.__transporte: Transporte = transporte
        self.__fabrica = fabrica
        self.__metaConductor = []
        self.__licencia = licencia
        transporte.setConductor(self)
        Conductor.listaConductores.append(self)
    
    def mostrarMetas(self) -> str:
        texto = []
        metas_no_verificadas = [meta for meta in self.metaConductor if not meta.getVerificador()] 

        for idx, meta in enumerate(metas_no_verificadas, start=1): 
            texto.append(f"\nMeta {idx}: {meta}")  
        return "".join(texto)  
    
    def __str__(self) -> str:
        return (f"\nNombre: {self.getNombre()}\n"
                f"Cedula: {self.getCedula()}\n"
                f"Edad: {self.getEdad()}\n"
                f"Transporte: {self.transporte.getTipoTransporte()}")
    
    def recibir_sueldo(self, valor: float):
        self.getCuentaBancaria().anadir_dinero(valor)
        self.setCantidadTrabajo(0)
    
    def getTransporte(self):
        return self.transporte
    
    def setTransporte(self, transporte):
        self.transporte = transporte
    
    def getFabrica(self):
        return self.fabrica
    
    def setFabrica(self, fabrica):
        self.fabrica = fabrica
    
    @classmethod
    def getListaConductores(cls):
        return cls.listaConductores
    
    def getMeta(self):
        return self.__metaConductor
    
    def setMetaConductor(self, meta):
        self.__metaConductor.append(meta)
    
    def aumentarCargaTrabajo(self):
        self.__cantidadTrabajo += 1
    
    def aumentarIndiceMeta(self, peso: float):
        self.setIndiceMeta(self.getIndiceMeta() + peso)
    
    def getLicencia(self) -> str:
        return self.__licencia
    
    def setLicencia(self, licencia: str):
        self.__licencia = licencia

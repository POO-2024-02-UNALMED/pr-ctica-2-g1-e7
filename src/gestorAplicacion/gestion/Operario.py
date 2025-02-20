from gestorAplicacion.gestion.Persona import Persona
class Operario(Persona):
    listaOperarios = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuentaBancaria, fabrica):
        super().__init__(nombre, cedula, edad, cuentaBancaria)
        self._fabrica = fabrica
        self._metaOperario = []
        Operario.listaOperarios.append(self)
    
    def mostrarMetas(self) -> str:
        texto = []
        metas_no_verificadas = [meta for meta in self._metaOperario if not meta._getVerificador()]  

        for idx, meta in enumerate(metas_no_verificadas, start=1): 
            texto.append(f"\nMeta {idx}: {meta}") 

        return "".join(texto)  

    def __str__(self) -> str:
        return (f"\nNombre: {self._getNombre()}\n"
                f"Cedula: {self._getCedula()}\n"
                f"Edad: {self._getEdad()}\n"
                f"Fabrica: {self._fabrica._getNombre() if self._fabrica else 'No asignada'}")
    
    def recibirSueldo(self, valor: float):
        self.getCuentaBancaria().añadirDinero(valor)
        self.setCantidadTrabajo(0)
    
    def setFabrica(self, fabrica):
        self._fabrica = fabrica
    
    def getFabrica(self):
        return self._fabrica
    
    def getMeta(self):
        return self._metaOperario
    
    def setMetaOperario(self, meta):
        self._metaOperario.append(meta)
    
    @classmethod
    def getListaOperarios(cls):
        return cls.listaOperarios

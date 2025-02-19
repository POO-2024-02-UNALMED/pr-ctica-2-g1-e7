from gestorAplicacion.gestion.Persona import Persona
class Operario(Persona):
    listaOperarios = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuentaBancaria, fabrica):
        super().__init__(nombre, cedula, edad, cuentaBancaria)
        self.fabrica = fabrica
        self.metaOperario = []
        Operario.listaOperarios.append(self)
    
    def mostrarMetas(self) -> str:
        texto = []
        for idx, meta in enumerate(self.metaOperario, start=1):
            if not meta.getVerificador():
                texto.append(f"\nMeta {idx} {meta}")
        return "".join(texto)
    
    def __str__(self) -> str:
        return (f"\nNombre: {self.getNombre()}\n"
                f"Cedula: {self.getCedula()}\n"
                f"Edad: {self.getEdad()}\n"
                f"Fabrica: {self.fabrica.getNombre() if self.fabrica else 'No asignada'}")
    
    def recibirSueldo(self, valor: float):
        self.getCuentaBancaria().añadirDinero(valor)
        self.setCantidadTrabajo(0)
    
    def setFabrica(self, fabrica):
        self.fabrica = fabrica
    
    def getFabrica(self):
        return self.fabrica
    
    def getMeta(self):
        return self.metaOperario
    
    def setMetaOperario(self, meta):
        self.metaOperario.append(meta)
    
    @classmethod
    def getListaOperarios(cls):
        return cls.listaOperarios

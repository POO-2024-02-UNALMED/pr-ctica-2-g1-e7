from gestion import Persona
from produccion import Transporte

class Conductor(Persona):
    lista_conductores = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuenta_bancaria, fabrica, transporte: Transporte, licencia: str = None):
        super().__init__(nombre, cedula, edad, cuenta_bancaria)
        self.transporte = transporte
        self.fabrica = fabrica
        self.meta_conductor = []
        self.licencia = licencia
        transporte.set_conductor(self)
        Conductor.lista_conductores.append(self)
    
    def mostrar_metas(self) -> str:
        texto = []
        for idx, meta in enumerate(self.meta_conductor, start=1):
            if not meta.get_verificador():
                texto.append(f"\nMeta {idx} {meta}")
        return "".join(texto)
    
    def __str__(self) -> str:
        return (f"\nNombre: {self.get_nombre()}\n"
                f"Cedula: {self.get_cedula()}\n"
                f"Edad: {self.get_edad()}\n"
                f"Transporte: {self.transporte.get_tipo_transporte()}")
    
    def recibir_sueldo(self, valor: float):
        self.get_cuenta_bancaria().anadir_dinero(valor)
        self.set_cantidad_trabajo(0)
    
    def get_transporte(self):
        return self.transporte
    
    def set_transporte(self, transporte: Transporte):
        self.transporte = transporte
    
    def get_fabrica(self):
        return self.fabrica
    
    def set_fabrica(self, fabrica):
        self.fabrica = fabrica
    
    @classmethod
    def get_lista_conductores(cls):
        return cls.lista_conductores
    
    def get_meta(self):
        return self.meta_conductor
    
    def set_meta_conductor(self, meta):
        self.meta_conductor.append(meta)
    
    def aumentar_carga_trabajo(self):
        self.cantidad_trabajo += 1
    
    def aumentar_indice_meta(self, peso: float):
        self.set_indice_meta(self.get_indice_meta() + peso)
    
    def get_licencia(self) -> str:
        return self.licencia
    
    def set_licencia(self, licencia: str):
        self.licencia = licencia

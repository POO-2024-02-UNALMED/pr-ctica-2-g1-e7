from Persona import Persona
class Operario(Persona):
    lista_operarios = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuenta_bancaria, fabrica):
        super().__init__(nombre, cedula, edad, cuenta_bancaria)
        self.fabrica = fabrica
        self.meta_operario = []
        Operario.lista_operarios.append(self)
    
    def mostrar_metas(self) -> str:
        texto = []
        for idx, meta in enumerate(self.meta_operario, start=1):
            if not meta.get_verificador():
                texto.append(f"\nMeta {idx} {meta}")
        return "".join(texto)
    
    def __str__(self) -> str:
        return (f"\nNombre: {self.get_nombre()}\n"
                f"Cedula: {self.get_cedula()}\n"
                f"Edad: {self.get_edad()}\n"
                f"Fabrica: {self.fabrica.get_nombre() if self.fabrica else 'No asignada'}")
    
    def recibir_sueldo(self, valor: float):
        self.get_cuenta_bancaria().anadir_dinero(valor)
        self.set_cantidad_trabajo(0)
    
    def set_fabrica(self, fabrica):
        self.fabrica = fabrica
    
    def get_fabrica(self):
        return self.fabrica
    
    def get_meta(self):
        return self.meta_operario
    
    def set_meta_operario(self, meta):
        self.meta_operario.append(meta)
    
    @classmethod
    def get_lista_operarios(cls):
        return cls.lista_operarios

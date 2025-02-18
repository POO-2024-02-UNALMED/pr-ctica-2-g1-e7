from gestorAplicacion.gestion.Persona import Persona

class Vendedor(Persona):
    lista_vendedores = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuenta_bancaria):
        super().__init__(nombre, cedula, edad, cuenta_bancaria)
        self.tienda = None
        self.meta_vendedor = []
        Vendedor.lista_vendedores.append(self)
    
    def mostrar_metas(self) -> str:
        texto = []
        for idx, meta in enumerate(self.meta_vendedor, start=1):
            if not meta.get_verificador():
                texto.append(f"\nMeta {idx} {meta}")
        return "".join(texto)
    
    def __str__(self) -> str:
        return (f"\nNombre: {self.get_nombre()}\n"
                f"Cedula: {self.get_cedula()}\n"
                f"Edad: {self.get_edad()}\n"
                f"Tienda: {self.tienda.get_nombre() if self.tienda else 'No asignada'}")
    
    def recibir_sueldo(self, valor: float):
        self.get_cuenta_bancaria().anadir_dinero(valor)
        self.set_cantidad_trabajo(0)
    
    def set_tienda(self, tienda):
        self.tienda = tienda
    
    def get_tienda(self):
        return self.tienda
    
    def get_meta(self):
        return self.meta_vendedor
    
    def set_meta_vendedor(self, meta):
        self.meta_vendedor.append(meta)
    
    @classmethod
    def get_lista_vendedores(cls):
        return cls.lista_vendedores
    
    def aumentar_carga_trabajo(self):
        self.cantidad_trabajo += 1
    
    def aumentar_indice_meta(self):
        self.set_indice_meta(self.get_indice_meta() + 1)

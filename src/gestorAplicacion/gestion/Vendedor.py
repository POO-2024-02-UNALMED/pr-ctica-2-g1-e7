from gestorAplicacion.gestion.Persona import Persona

class Vendedor(Persona):
    listaVendedores = []
    
    def __init__(self, nombre: str, cedula: int, edad: int, cuentaBancaria):
        super().__init__(nombre, cedula, edad, cuentaBancaria)
        self.__tienda = None
        self.__metaVendedor = []
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
        self.__tienda = tienda
    
    def getTienda(self):
        return self.__tienda
    
    def getMeta(self):
        return self.__metaVendedor
    
    def setMetaVendedor(self, meta):
        self.__metaVendedor.append(meta)
    
    @classmethod
    def getListaVendedores(cls):
        return cls.listaVendedores
    
    def aumentarCargaTrabajo(self):
        self.__cantidadTrabajo += 1
    
    def aumentarIndiceMeta(self):
        self.setIndiceMeta(self.getIndiceMeta() + 1)

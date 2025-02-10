from Persona import Persona

class Vendedor(Persona):
    listaVendedores = []  # Lista de todos los vendedores

    def __init__(self, nombre=None, cedula=None, edad=None, cuentaBancaria=None):
        if nombre is not None and cedula is not None and edad is not None and cuentaBancaria is not None:
            super().__init__(nombre, cedula, edad, cuentaBancaria)
            self.tienda = None       # Atributo que se puede asignar posteriormente
            self.metaVendedor = []
            Vendedor.listaVendedores.append(self)
        else:
            # Constructor vacío
            pass

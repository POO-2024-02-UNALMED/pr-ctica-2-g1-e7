from produccion import Producto
class Cliente:
    listaClientes = []      # Variable de clase: lista de todos los clientes
    totalCreados = 0        # Variable de clase: contador de clientes creados

    def __init__(self, nombre=None, edad=None, cedula=None, cuentaBancaria=None):
        if nombre is not None and edad is not None and cedula is not None and cuentaBancaria is not None:
            self.nombre = nombre
            self.edad = edad
            self.cedula = cedula
            self.cuentaBancaria = cuentaBancaria
            self.listaFacturas = []   # Lista de facturas
            self.listaProductos = []  # Lista de productos
            self.id = Cliente.totalCreados
            Cliente.totalCreados += 1
            Cliente.listaClientes.append(self)
        else:
            # Constructor vacío (sin parámetros)
            pass
    
    def removerProducto(self, producto: Producto):
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que remueve un producto de la lista de productos del cliente.
        """
        if producto in self.listaProductos:
            self.listaProductos.remove(producto)

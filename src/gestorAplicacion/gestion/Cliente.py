from produccion import Producto
class Cliente:
    listaClientes = []      # Variable de clase: lista de todos los clientes
    totalCreados = 0        # Variable de clase: contador de clientes creados

    def __init__(self, nombre=None, edad=None, cedula=None, cuentaBancaria=None):
        if all(param is not None for param in [nombre, edad, cedula, cuentaBancaria]):
            self._nombre = nombre
            self._edad = edad
            self._cedula = cedula
            self._cuentaBancaria = cuentaBancaria
            self._listaFacturas = []  
            self._listaProductos = []  
            self._id = Cliente.totalCreados
            Cliente.totalCreados += 1
            Cliente.listaClientes.append(self)
    
    # Método de la funcionalidad enviarPedidos:
    # Retorna una lista de clientes numerada, facilitando la selección por parte del usuario.
    # Formato de salida: "1. NombreCliente"
    @staticmethod
    def mostrarClientes():
        if not Cliente.listaClientes:
            return "No hay clientes registrados."
        
        texto = ""
        for i, cliente in enumerate(Cliente.listaClientes, start=1):
            texto += f"{i}. {cliente.getNombre()}\n"
        return texto
    # Getters
    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getCedula(self):
        return self._cedula

    def getCuentaBancaria(self):
        return self._cuentaBancaria

    def getListaFacturas(self):
        return self._listaFacturas

    def getListaProductos(self):
        return self._listaProductos

    def getId(self):
        return self._id

    # Setters
    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setCedula(self, cedula):
        self._cedula = cedula

    def setCuentaBancaria(self, cuentaBancaria):
        self._cuentaBancaria = cuentaBancaria

    def setListaFacturas(self, listaFacturas):
        self._listaFacturas = listaFacturas

    def setListaProductos(self, listaProductos):
        self._listaProductos = listaProductos

    
    def removerProducto(self, producto: Producto):
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que remueve un producto de la lista de productos del cliente.
        """
        if producto in self.listaProductos:
            self.listaProductos.remove(producto)

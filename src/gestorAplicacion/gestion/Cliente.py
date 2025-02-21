class Cliente:
    listaClientes = []      # Variable de clase: lista de todos los clientes
    totalCreados = 0        # Variable de clase: contador de clientes creados

    def __init__(self, nombre=None, edad=None, cedula=None, cuentaBancaria=None):
        if all(param is not None for param in [nombre, edad, cedula, cuentaBancaria]):
            self.__nombre = nombre
            self._nombre = self.__nombre
            self.__edad = edad
            self.__cedula = cedula
            self.__cuentaBancaria = cuentaBancaria
            self.__listaFacturas = []  
            self.__listaProductos = []  
            self.__id = Cliente.totalCreados
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
        return self.__edad

    def getCedula(self):
        return self.__cedula

    def getCuentaBancaria(self):
        return self.__cuentaBancaria

    def getListaFacturas(self):
        return self.__listaFacturas

    def getListaProductos(self):
        return self.__listaProductos

    def getId(self):
        return self.__id

    # Setters
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = edad

    def setCedula(self, cedula):
        self.__cedula = cedula

    def setCuentaBancaria(self, cuentaBancaria):
        self.__cuentaBancaria = cuentaBancaria

    def setListaFacturas(self, listaFacturas):
        self.__listaFacturas = listaFacturas

    def setListaProductos(self, listaProductos):
        self.__listaProductos = listaProductos
    
   
    
    def removerProducto(self, producto):
        from gestorAplicacion.produccion.Producto import Producto
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que remueve un producto de la lista de productos del cliente.
        """
        if producto in self.__listaProductos:
            self.__listaProductos.remove(producto)
            
from gestorAplicacion.gestion.CuentaBancaria import CuentaBancaria


cuentaCliente1 = CuentaBancaria(10001, 5000)
cuentaCliente2 = CuentaBancaria(10002, 15000)
cuentaCliente3 = CuentaBancaria(10003, 8000)
cuentaCliente4 = CuentaBancaria(10004, 2000)
cuentaCliente5 = CuentaBancaria(10005, 12000)

cliente1 = Cliente("Juan Pérez", 30, 987654321, cuentaCliente1)
cliente2 = Cliente("María López", 25, 123456789, cuentaCliente2)
cliente3 = Cliente("Carlos García", 40, 567890123, cuentaCliente3)
cliente4 = Cliente("Ana Rodríguez", 35, 654321987, cuentaCliente4)
cliente5 = Cliente("Luis Fernández", 28, 192837465, cuentaCliente5)



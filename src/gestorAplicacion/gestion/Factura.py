from datetime import date
import Cliente
from produccion import Tienda, Transporte, Producto, EstadoProducto
from .IMostrarProductos import mostrarProductosFactura 

class Factura:
    # Variables de clase (atributos estáticos)
    totalCreadas = 0
    listaFacturas = []

    def __init__(self, tienda, cliente, transporte, lista_productos, precio_envio, fecha: date):
        self.tienda = tienda
        self.cliente = cliente
        self.transporte = transporte
        self.listaProductos = lista_productos
        self.precioEnvio = precio_envio

        # Si ya existen más de dos facturas, se ordenan por fecha.
        if len(Factura.lista_facturas) > 2:
            Factura.ordenar_facturas_por_fecha()

        self.fecha = fecha
        self.total = self.calcular_total()

        # Se incrementa el contador y se asigna el id
        Factura.total_creadas += 1
        self.id = Factura.total_creadas

        # Se agrega la factura a la lista de facturas
        Factura.lista_facturas.append(self)

    
    @classmethod
    def ordenar_facturas_por_fecha(cls):
        """
        Método que ordena la lista de facturas (lista_facturas) utilizando
        el algoritmo de la burbuja, comparando la propiedad 'fecha'.
        """
        n = len(cls.lista_facturas)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if cls.lista_facturas[j].fecha > cls.lista_facturas[j + 1].fecha:
                    # Intercambio de posiciones
                    cls.lista_facturas[j], cls.lista_facturas[j + 1] = cls.lista_facturas[j + 1], cls.lista_facturas[j]

    @classmethod
    def mostrarFacturas(cls): 
        string=""
        n=1
        for factura in Factura.lista_facturas: 
            string+= str(n),". ", factura.getCliente().getNombre(), "ID: ", factura.getID() 
            n+=1
        return string 
    
    @classmethod
    def seleccionarFactura(cls,num:int):
        return cls.listaFacturas[num-1] 

    def mostrarProductosFactura(self): 
        return mostrarProductosFactura(self)
    
    def todosDevueltos(self) -> bool:
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que se encarga de verificar si todos los productos de una factura han sido devueltos o no.
        """
        return all(p.estado == EstadoProducto.DEVUELTO for p in self.listaProductos)
    
    def seleccionarProducto(self, n: int):
        """
        Método que selecciona un producto de la lista basado en el índice proporcionado.
        """
        if 1 <= n <= len(self.listaProductos):
            return self.listaProductos[n - 1]
        return None 
    #Manejar con una excepcion cuando el entero pasado está por fuera del rango establecido. !!
    
    
    
    #getters y setters
    def getCliente(self): 
        return self.cliente
    def getListaProductos(self): 
        return self.listaProductos

from datetime import date
import Cliente
from produccion import Tienda, Transporte, Producto

class Factura:
    # Variables de clase (atributos estáticos)
    totalCreadas = 0
    listaFacturas = []

    def __init__(self, tienda, cliente, transporte, lista_productos, precio_envio, fecha: date):
        self.tienda = tienda
        self.cliente = cliente
        self.transporte = transporte
        self.listaProductos = lista_productos
        self.precio_envio = precio_envio

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

    def calcular_total(self):
        """
        Método para calcular el total de la factura.
        Se asume que cada producto en 'lista_productos' tiene un atributo 'precio'.
        Esta implementación suma el precio de cada producto y le añade el precio de envío.
        Modifica la lógica según las reglas de negocio reales.
        """
        total_productos = sum(getattr(producto, 'precio', 0) for producto in self.lista_productos)
        return total_productos + self.precio_envio

    @classmethod
    def ordenar_facturas_por_fecha(cls):
        """
        Método que ordena la lista de facturas (lista_facturas) utilizando
        el algoritmo de la burbuja, comparando la propiedad 'fecha'.
        Se asume que 'fecha' es un objeto comparable (por ejemplo, datetime.date).
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
        return cls.lista_facturas[num-1] 

    def mostrarProductos(self): 
        for producto in self.listaProductos: 
            




    #getters y setters
    def getCliente(self): 
        return self.cliente


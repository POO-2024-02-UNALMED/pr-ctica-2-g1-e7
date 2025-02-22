from datetime import datetime
from gestorAplicacion.gestion.IMostrarProductos import IMostrarProductos

class Factura(IMostrarProductos):
    # Variables de clase (atributos estáticos)
    totalCreadas = 0
    listaFacturas = []

    def __init__(self, tienda, cliente, transporte, lista_productos: list, precio_envio: float, fecha: datetime):
        self._tienda = tienda
        self._cliente = cliente
        self._transporte = transporte
        self._listaProductos = lista_productos
        self._precioEnvio = precio_envio

        # Si ya existen más de dos facturas, se ordenan por fecha.
        if len(Factura.getListaFacturas()) > 2:
            Factura.ordenar_facturas_por_fecha()
        if type(fecha) is not datetime:
            self._fecha = self.convertirFecha(fecha)
        self._fecha = fecha
        self._total = self.calcularTotal()

        # Se incrementa el contador y se asigna el id
        Factura.totalCreadas += 1
        self._id = Factura.totalCreadas

        # Se agrega la factura a la lista de facturas
        Factura.listaFacturas.append(self)

    
    @classmethod
    def ordenar_facturas_por_fecha(cls):
        """
        Método que ordena la lista de facturas (lista_facturas) utilizando
        el algoritmo de la burbuja, comparando la propiedad 'fecha'.
        """
        n = len(cls.listaFacturas)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if cls.listaFacturas[j].getFecha() > cls.lista_facturas[j + 1].getFecha():
                    # Intercambio de posiciones
                    cls.listaFacturas[j], cls.lista_facturas[j + 1] = cls.lista_facturas[j + 1], cls.lista_facturas[j]

    @classmethod
    def mostrarFacturas(cls): 
        string=""
        n=1
        for factura in Factura.listaFacturas: 
            string+= str(n),". ", factura.getCliente().getNombre(), "ID: ", factura.getID() 
            n+=1
        return string 
    
    @classmethod
    def seleccionarFactura(cls,num:int):
        return cls.listaFacturas[num-1] 
    
    def calcularTotal(self): 
        total=0
        for producto in self._listaProductos: 
            total+=producto.getPrecio()
        return total

        
    
    def todosDevueltos(self) -> bool:
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que se encarga de verificar si todos los productos de una factura han sido devueltos o no.
        """
        return all(p.getDevuelto() for p in self._listaProductos)
    
    def seleccionarProducto(self, n: int):
        """
        Método que selecciona un producto de la lista basado en el índice proporcionado.
        """
        if 1 <= n <= len(self._listaProductos):
            return self._listaProductos[n - 1]
        return None 
    #Manejar con una excepcion cuando el entero pasado está por fuera del rango establecido. !!
    
    #Métodos para la funcionalidad estadística

    def convertirFecha(self, fecha: datetime) -> datetime:
        """
        Método que convierte una cadena de texto en una fecha.
        """
        return fecha.strptime("%dd-%mm-%yyyy")
    
    @staticmethod
    def getFechaMinima() -> datetime:
        """
        Método que obtiene la fecha mínima de la factura.
        """
        return Factura.listaFacturas[0].getFecha()
        #return min(f.getFecha() for f in Factura.listaFacturas)
    
    @staticmethod
    def getFechaMaxima() -> datetime:
        """
        Método que obtiene la fecha máxima de la factura.
        """
        return Factura.listaFacturas[-1].getFecha()
        #return max(f.getFecha() for f in Factura.listaFacturas)
    
    @staticmethod
    def getFacturasEntreFechas(fecha_min: datetime, fecha_max: datetime):
        """
        Método que obtiene las facturas que se encuentran entre dos fechas.
        """
        return [f for f in Factura.getListaFacturas() if fecha_min <= f.getFecha() <= fecha_max]
    
    def getListaFechas(self, fecha_min: datetime, fecha_max: datetime):
        """
        Método que obtiene una lista de fechas entre dos fechas.
        """
        return [f.getFecha() for f in Factura.lista_facturas if fecha_min <= f.getFecha() <= fecha_max]
    
    @staticmethod
    def gananciasDiscretas(fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula las ganancias entre dos fechas.
        """
        facturas = Factura.getFacturasEntreFechas(fecha_min, fecha_max)
        ganancias: list[list[datetime, float]] = []
        for f in facturas:
            ganancias.append([f.getFecha(), f.getTotal()])
        return ganancias
    
    @staticmethod
    def gananciaTotal(fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula la ganancia total entre dos fechas.
        """
        facturas = Factura.getFacturasEntreFechas(fecha_min, fecha_max)
        return sum(f.getTotal() for f in facturas)
    
    @staticmethod
    def promedioDeGanancias(fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula el promedio de ganancias entre dos fechas.
        """
        facturas = Factura.getFacturasEntreFechas(fecha_min, fecha_max)
        return sum(f.getTotal() for f in facturas) / len(facturas)
    
    @staticmethod
    def aumentosPorcentuales(fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula los aumentos porcentuales entre dos fechas.
        """
        facturas = Factura.getFacturasEntreFechas(fecha_min, fecha_max)
        aumentos = []
        for i in range(1, len(facturas)):
            aumento = (facturas[i].getTotal() - facturas[i - 1].getTotal()) / facturas[i - 1].getTotal() * 100
            aumentos.append([facturas[i].getFecha(), aumento])
        return aumentos
    
    @staticmethod
    def modaProductos(fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula la moda de los productos.
        """
        productos = [p.getNombre() for f in Factura.getFacturasEntreFechas(fecha_min, fecha_max) for p in f.getListaProductos()]
        moda = max(set(productos), key=productos.count)
        return moda
    
    @staticmethod
    def modaClientes(fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula la moda de los clientes.
        """
        clientes = [f.getCliente().getNombre() for f in Factura.getFacturasEntreFechas(fecha_min, fecha_max)]
        moda = max(set(clientes), key=clientes.count)
        return moda
    
    @staticmethod
    def modaTiendas(fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula la moda de las tiendas.
        """
        tiendas = [f.getTienda().getNombre() for f in Factura.getFacturasEntreFechas(fecha_min, fecha_max)]
        moda = max(set(tiendas), key=tiendas.count)
        return moda
    
        
    def __str__(self):
        factura = []
        totalPrecio = 0
        totalPeso = 0
        precioEnvio = self._precioEnvio

        # Borde superior
        factura.append("=====================================\n")
        factura.append("|                                   |\n")
        factura.append(f"| {self._tienda.getNombre():<33} |\n")
        factura.append("|                                   |\n")
        factura.append("=====================================\n")

        # Encabezado del cliente y detalles
        factura.append(f"| ID Factura: {self._id:<24} |\n")
        factura.append(f"| Cliente: {self._cliente.getNombre():<26} |\n")
        factura.append(f"| Cédula: {self._cliente.getCedula():<26} |\n")
        factura.append(f"| Fecha: {self._fecha.strftime('%Y-%m-%d'):<28} |\n")
        factura.append(f"| Transporte: {self._transporte.getTipoTransporte().getNombre():<22} |\n")
        factura.append("========================================================\n")

        # Encabezado de los productos
        factura.append("| Producto                     | Precio    | Peso (kg) |\n")
        factura.append("|------------------------------|-----------|-----------|\n")

        # Detalles de los productos
        for producto in self._listaProductos:
            if producto is not None:
                factura.append(f"| {producto.getNombre():<28} | ${producto.getPrecio():<8.2f} | {producto.getPeso():<8.2f} |\n")
                totalPrecio += producto.getPrecio()
                totalPeso += producto.getPeso()

        # Totales
        totalPrecio += precioEnvio
        factura.append("|------------------------------|-----------|-----------|\n")
        factura.append(f"| Envío                       | ${precioEnvio:<8.2f} | {'N/A':<8} |\n")
        factura.append(f"| Total                       | ${totalPrecio:<8.2f} | {totalPeso:<8.2f} |\n")
        factura.append("=======================================================\n")

        return ''.join(factura)

    #getters:
    def getCliente(self): 
        return self._cliente
    def getListaProductos(self): 
        return self._listaProductos

    def getID(self):
        return self._id
    
    def getFecha(self):
        return self._fecha
    
    def getTotal(self):
        return self._total
    
    def getTransporte(self):
        return self._transporte
    
    def getTienda(self):
        return self._tienda
    
    def getPrecioEnvio(self):
        return self._precioEnvio
    
    def getListaProductos(self):
        return self._listaProductos
    
    @staticmethod
    def getListaFacturas():
        return Factura.listaFacturas
    
    @staticmethod
    def getTotalCreadas():
        return Factura.totalCreadas
    

    #setters:
    def setCliente(self, cliente): 
        self._cliente=cliente

    def setListaProductos(self, listaProductos):
        self._listaProductos=listaProductos

    def setID(self, id):
        self._id=id

    def setFecha(self, fecha):
        self._fecha=fecha

    def setTienda(self, tienda):
        self._tienda=tienda

    def setCliente(self, cliente):
        self._cliente=cliente

    def setTransporte(self, transporte):
        self._transporte=transporte

    def setPrecioEnvio(self, precioEnvio):
        self._precioEnvio=precioEnvio

    @staticmethod
    def setTotalCreadas(cls, totalCreadas):
        cls.totalCreadas=totalCreadas

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
        if len(Factura.listaFacturas) > 2:
            Factura.ordenar_facturas_por_fecha()

        self.fecha = fecha
        self.total = self.calcularTotal()

        # Se incrementa el contador y se asigna el id
        Factura.totalCreadas += 1
        self.id = Factura.totalCreadas

        # Se agrega la factura a la lista de facturas
        Factura.listaFacturas.append(self)

    
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
    
    def calcularTotal(self): 
        from gestorAplicacion.produccion.Producto import Producto
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
        if 1 <= n <= len(self.listaProductos):
            return self.listaProductos[n - 1]
        return None 
    #Manejar con una excepcion cuando el entero pasado está por fuera del rango establecido. !!
    
    #Métodos para la funcionalidad estadística

    def convertirStrAFecha(self, fecha: str) -> datetime:
        """
        Método que convierte una cadena de texto en una fecha.
        """
        return datetime.strptime(fecha, "%d-%m-%y %H:%M:%S")
    
    def getFechaMinima(self) -> datetime:
        """
        Método que obtiene la fecha mínima de la factura.
        """
        return min(p.fecha for p in self.listaProductos)
    
    def getFechaMaxima(self) -> datetime:
        """
        Método que obtiene la fecha máxima de la factura.
        """
        return max(p.fecha for p in self.listaProductos)
    
    def getFacturasEntreFechas(self, fecha_min: datetime, fecha_max: datetime):
        """
        Método que obtiene las facturas que se encuentran entre dos fechas.
        """
        return [f for f in Factura.lista_facturas if fecha_min <= f.fecha <= fecha_max]
    
    def getListaFechas(self, fecha_min: datetime, fecha_max: datetime):
        """
        Método que obtiene una lista de fechas entre dos fechas.
        """
        return [f.fecha for f in Factura.lista_facturas if fecha_min <= f.fecha <= fecha_max]
    
    def gananciasDiscretas(self, fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula las ganancias entre dos fechas.
        """
        facturas = self.getFacturasEntreFechas(fecha_min, fecha_max)
        ganancias: list[list[datetime, float]] = []
        for f in facturas:
            ganancias.append([f.fecha, f.total])
        return ganancias
    
    def gananciaTotal(self, fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula la ganancia total entre dos fechas.
        """
        facturas = self.getFacturasEntreFechas(fecha_min, fecha_max)
        return sum(f.total for f in facturas)
    
    def promedioDeGanancias(self, fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula el promedio de ganancias entre dos fechas.
        """
        facturas = self.getFacturasEntreFechas(fecha_min, fecha_max)
        return sum(f.total for f in facturas) / len(facturas)
    
    def aumentosPorcentuales(self, fecha_min: datetime, fecha_max: datetime):
        """
        Método que calcula los aumentos porcentuales entre dos fechas.
        """
        facturas = self.getFacturasEntreFechas(fecha_min, fecha_max)
        aumentos = []
        for i in range(1, len(facturas)):
            aumento = (facturas[i].total - facturas[i - 1].total) / facturas[i - 1].total * 100
            aumentos.append([facturas[i].fecha, aumento])
        return aumentos
    
    def modaProductos(self):
        """
        Método que calcula la moda de los productos.
        """
        productos = [p.nombre for p in self.listaProductos]
        moda = max(set(productos), key=productos.count)
        return moda
    
    def modaClientes(self):
        from gestion.Cliente import Cliente
        """
        Método que calcula la moda de los clientes.
        """
        clientes = [f.cliente.nombre for f in Factura.lista_facturas]
        moda = max(set(clientes), key=clientes.count)
        return moda
    
    def modaTiendas(self):
        """
        Método que calcula la moda de las tiendas.
        """
        tiendas = [f.tienda.nombre for f in Factura.lista_facturas]
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
        factura.append(f"| ID Factura: {self.id:<24} |\n")
        factura.append(f"| Cliente: {self._cliente.getNombre():<26} |\n")
        factura.append(f"| Cédula: {self._cliente.getCedula():<26} |\n")
        factura.append(f"| Fecha: {self.fecha.strftime('%Y-%m-%d'):<28} |\n")
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

    #getters y setters
    def getCliente(self): 
        return self._cliente
    def getListaProductos(self): 
        return self._listaProductos
    def getTienda(self): 
        return self._tienda
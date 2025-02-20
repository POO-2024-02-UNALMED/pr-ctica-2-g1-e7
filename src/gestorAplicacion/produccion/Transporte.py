
class Transporte:
    montoEnvioGratis = 3000
    listaTransportes = []  # Lista de transportes


    def __init__(self, tipoTransporte=None, capacidad=None, costo=None):
        if tipoTransporte is not None and capacidad is not None and costo is not None:
            self.__tipoTransporte = tipoTransporte  # Se espera que sea una instancia de TipoTransporte
            self.__capacidad = capacidad
            self.__costo = costo
            self.__listaDeProductos = []  # Lista de productos a transportar
            self.__conductor = None
            self.__tienda= None
            Transporte.listaTransportes.append(self)
        else:
            # Constructor vacío
            self.listaTransportes = []
            self.__listaDeProductos = []
    def abastecerProducto(self, tiendaSeleccionada, productosSeleccionados):
        """
        Carga productos en el transporte y asigna la tienda de destino.
        """
        self.getListaDeProductos().extend(productosSeleccionados)
        self.tienda = tiendaSeleccionada
    # Método estático perteneciente a la funcionalidad enviarPedidos:
    # Calcula y devuelve el peso total de una lista de productos, sumando solo los productos con peso positivo.
    # Si un producto tiene un peso inválido (no positivo), muestra un mensaje de error.
    @staticmethod
    def calcularTotalPeso(listaProductosPedidos):
        from gestorAplicacion.produccion.Producto import Producto
        totalPeso = 0
        for producto in listaProductosPedidos:
            peso = producto.getPeso()
            if peso > 0:  # Validamos que el peso sea positivo
                totalPeso += peso
            else:
                print(f"\nError: Peso inválido para el producto {producto.nombre}")
        return totalPeso
    @staticmethod
    def enviarGratis(listaProductos):
        from gestorAplicacion.produccion.Producto import Producto
        precioTotal = sum(producto.getPrecio() for producto in listaProductos)
        return precioTotal > Transporte.montoEnvioGratis
    
    def getTipoTransporte(self):
        return self.__tipoTransporte

    def setTipoTransporte(self, tipoTransporte):
        self.__tipoTransporte = tipoTransporte

    def getCapacidad(self):
        return self.__capacidad

    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad

    def getCosto(self):
        return self.__costo

    def setCosto(self, costo):
        self.__costo = costo

    def getListaDeProductos(self):
        return self.__listaDeProductos

    def setListaDeProductos(self, listaDeProductos):
        self.__listaDeProductos = listaDeProductos

    def getConductor(self):
        return self.__conductor

    def setConductor(self, conductor):
        self.__conductor = conductor

    def getTienda(self):
        return self.__tienda

    def setTienda(self, tienda):
        self.__tienda = tienda

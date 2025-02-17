from typing import List
class Tienda():

    numTiendas = 0  # Contador de tiendas

    def __init__(self, nombre=None, vendedor=None, cuentaBancaria=None,
                 capacidadMaximaMaterial=None, capacidadMaximaConsumible=None,
                 capacidadMaximaLimpieza=None):

        if all(param is not None for param in [nombre, vendedor, cuentaBancaria,
                                               capacidadMaximaMaterial, capacidadMaximaConsumible,
                                               capacidadMaximaLimpieza]):
            self.__nombre = nombre
            self.__vendedor = vendedor
            self.__cuentaBancaria = cuentaBancaria
            self.__capacidadMaximaMaterial = capacidadMaximaMaterial
            self.__capacidadMaximaConsumible = capacidadMaximaConsumible
            self.__capacidadMaximaLimpieza = capacidadMaximaLimpieza

            # Se asigna la tienda al vendedor si tiene el método
            if hasattr(vendedor, "setTienda"):
                vendedor.setTienda(self)

            Tienda.numTiendas += 1

            self.__listaProducto = []
            self.__productosPorCategoria = []
            self.__categorias = []
            self.__conteoCategorias = []

    # Getters
    def getNombre(self):
        return self.__nombre

    def getVendedor(self):
        return self.__vendedor

    def getCuentaBancaria(self):
        return self.__cuentaBancaria

    def getListaProducto(self):
        return self.__listaProducto

    def getProductosPorCategoria(self):
        return self.__productosPorCategoria

    def getCategorias(self):
        return self.__categorias

    def getConteoCategorias(self):
        return self.__conteoCategorias

    # Setters
    def setNombre(self, nuevoNombre):
        if isinstance(nuevoNombre, str):
            self.__nombre = nuevoNombre
        else:
            raise ValueError("El nombre debe ser una cadena")

    def setVendedor(self, nuevoVendedor):
        self.__vendedor = nuevoVendedor

    def setCuentaBancaria(self, nuevaCuenta):
        if isinstance(nuevaCuenta, str):
            self.__cuentaBancaria = nuevaCuenta
        else:
            raise ValueError("La cuenta bancaria debe ser una cadena")

    def setListaProducto(self, nuevaLista):
        if isinstance(nuevaLista, list):
            self.__listaProducto = nuevaLista
        else:
            raise ValueError("La lista de productos debe ser una lista")

    def setProductosPorCategoria(self, nuevaLista):
        if isinstance(nuevaLista, list):
            self.__productosPorCategoria = nuevaLista
        else:
            raise ValueError("La lista de productos por categoría debe ser una lista")

    def setCategorias(self, nuevaLista):
        if isinstance(nuevaLista, list):
            self.__categorias = nuevaLista
        else:
            raise ValueError("La lista de categorías debe ser una lista")

    def setConteoCategorias(self, nuevaLista):
        if isinstance(nuevaLista, list):
            self.__conteoCategorias = nuevaLista
        else:
            raise ValueError("La lista de conteo de categorías debe ser una lista")
    



    def devolverProducto(self, factura, producto):
        from Producto import Producto
        producto: Producto = producto
        from gestion.Factura import Factura
        from produccion.EstadoProducto import EstadoProducto
        factura: Factura = factura
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que se encarga de procesar la devolución de un producto.
        """
        self.listaProducto.append(producto)
        producto.estado = EstadoProducto.DEVUELTO
        return factura.cliente 

    
    def mostrarProductos(self, producto):
        """
        Sobreescribe el método por defecto de la clase abstracta IMostrarProducto
        Método que muestra la lista de productos omitiendo el producto dado.
        """
        return [p for p in self.listaProducto if p.producto_id != producto.producto_id]
    from typing import List
    # Método de la funcionalidad enviarPedidos:
    # Crea una lista con los productos disponibles en la tienda y la cantidad de cada uno.
    # Si un producto ya existe en la lista, incrementa su contador; de lo contrario, lo agrega como un nuevo elemento.
    def listaProductosTienda(self):
        listaProductos = []
        
        for producto in self._listaProducto:
            encontrado = False
            if not listaProductos:
                listaProductos.append([producto, 1])
            else:
                for listaAux in listaProductos:
                    if listaAux[0].nombre == producto.nombre:
                        listaAux[1] += 1
                        encontrado = True
                        break
                
                if not encontrado:
                    listaProductos.append([producto, 1])
        
        return listaProductos

    # Método de la funcionalidad enviarPedidos:
    # Muestra la lista de productos disponibles en la tienda, incluyendo su nombre, precio, cantidad y peso.
    # Si la lista está vacía, devuelve un mensaje indicando que no hay productos registrados.
    def mostrarListaProductosTienda(self, listaProductos):
        if not listaProductos:
            return "Actualmente no hay productos registrados en el sistema."

        texto = []
        for i, listaAux in enumerate(listaProductos, start=1):
            producto, cantidad = listaAux
            texto.append(f"{i}. Producto: {producto.nombre}")
            texto.append(f" - Precio: {producto.precio}")
            texto.append(f" - Cantidad: {cantidad}")
            texto.append(f" - Peso: {producto.peso}\n")

        return "\n".join(texto).strip()

    # Método de la funcionalidad enviarPedidos:
    # Elimina de la tienda los productos cuyos nombres coincidan con los de la lista recibida.
    def eliminarProductosPorNombre(self, listaEliminar):
        
        self._listaProducto = [producto for producto in self._listaProducto if producto.nombre not in {p.nombre for p in listaEliminar}]

    # Método de la funcionalidad enviarPedidos:
    # Genera una factura con los productos seleccionados para el pedido, junto con el cliente, el transporte y el precio de envío.
    # Devuelve la factura en formato de texto.
    def enviarPedido(self, listaProductosPedidos, transporteSeleccionado, clienteSeleccionado, precioEnvio, dia):
        from gestion.Factura import Factura
        factura = Factura(self, clienteSeleccionado, transporteSeleccionado, listaProductosPedidos, precioEnvio, dia)
        return str(factura)

    

class Tienda:
    def __init__(self):
        self.listaProducto = []

    def agregar_productos_para_cambio(self, precio_cambio: float, seleccion_productos: List[int], productos_disponibles):
        from Producto import Producto
        """
        Funcionalidad: Devoluciones
        Método principal para gestionar los productos seleccionados para un cambio.

        :param precio_cambio: El valor máximo permitido para el cambio.
        :param seleccion_productos: Lista de índices seleccionados por el cliente.
        :param productos_disponibles: Lista de productos disponibles.
        :return: Lista de productos seleccionados para el cambio.
        """
        productos_seleccionados = []
        subtotal = 0.0

        for indice in seleccion_productos:
            # Validar índice y obtener el producto correspondiente
            if indice < 1 or indice > len(productos_disponibles):
                continue  # Ignorar índices inválidos

            producto_seleccionado = productos_disponibles[indice - 1]

            # Agregar el producto al carrito sin verificar duplicados
            productos_seleccionados.append(producto_seleccionado)
            subtotal += producto_seleccionado.precio

            # Verificar si el subtotal supera el precio permitido
            if subtotal > precio_cambio:
                break

        return productos_seleccionados

    
    def productosPorCategoria(self, productos, conteoTemporal=None):
        from Producto import Producto
        productos: List[Producto] = productos
        """
        Muestra los productos por categoría en formato: (cantidad actual/capacidad máxima).
        Si `conteoTemporal` se proporciona, se usa en lugar del conteo normal.
        """
        # Limpiar listas antes de procesar
        self.categorias = []

        # Lista de todas las categorías posibles
        todasLasCategorias = ["Herramientas", "Muebles", "Aseo"]
        
        # Inicializar las categorías
        for categoria in todasLasCategorias:
            self.categorias.append(categoria)
        
        # Si `conteoTemporal` no se proporciona, inicializar `conteoCategorias`
        if conteoTemporal is None:
            self.conteoCategorias = []
            self.conteoCategorias = [0] * len(self.categorias)

            # Contar productos por categoría
            for producto in productos:
                categoria = producto.getCategoria()  # Obtener la categoría
                if categoria in self.categorias:
                    index = self.categorias.index(categoria)
                    self.conteoCategorias[index] += 1
        else:
            # Si `conteoTemporal` existe, solo asegurarse de que las categorías están en la lista
            for producto in productos:
                categoria = producto.getCategoria()
                if categoria not in self.categorias:
                    self.categorias.append(categoria)

        # Construir el resultado
        resultado = ""
        for i, categoria in enumerate(self.categorias):
            conteo = self.conteoCategorias[i] if conteoTemporal is None else conteoTemporal[i]
            resultado += f"{categoria}: {conteo}/"

            # Agregar la capacidad máxima correspondiente
            if categoria == "Herramientas":
                resultado += str(self.capacidadMaximaMaterial)
            elif categoria == "Muebles":
                resultado += str(self.capacidadMaximaConsumible)
            elif categoria == "Aseo":
                resultado += str(self.capacidadMaximaLimpieza)
            else:
                resultado += "N/A"

            resultado += " productos\n"
        return resultado
    def getCantidadActualPorCategoria(self, categoria):
        cantidad = sum(1 for producto in self.listaProducto if producto.getCategoria() == categoria)
        return cantidad
    def cantidadProductos(self):
        """
        Muestra los productos de la tienda de forma ordenada (producto: cantidad).
        """
        nombresContados = []
        resultado = ""

        for producto in self.listaProducto:
            if producto.getNombre() not in nombresContados:
                cantidad = sum(1 for p in self.listaProducto if p.getNombre() == producto.getNombre())
                nombresContados.append(producto.getNombre())
                resultado += f"{producto.getNombre()}: {cantidad} unidades\n"

        return resultado

    def descargarProducto(self, transporteSeleccionado):
        """
        Descarga los productos transportados a la tienda y vacía la lista del transporte.
        """
        productosTransportados = transporteSeleccionado.getListaDeProductos()
        self.listaProducto.extend(productosTransportados)
        transporteSeleccionado.getListaDeProductos().clear()  # Vaciar la lista de productos del transporte
        

from Producto import Producto
tienda = Tienda()
tienda.productosPorCategoria([Producto("Martillo", 10, "Herramientas"), Producto("Silla", 20, "Muebles"), Producto("Escoba", 30, "Aseo")])
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

 # Importar Fabrica al inicio

class Tienda:
    numTiendas = 0 # Atributo estático para contar el número de tiendas

    def __init__(self, nombre, vendedor, cuentaBancaria,
                 capacidadMaximaMaterial, capacidadMaximaConsumible,
                 capacidadMaximaLimpieza):
        """
        Constructor de la clase Tienda.
        :param nombre: Nombre de la tienda.
        :param vendedor: Vendedor asignado a la tienda.
        :param cuentaBancaria: Cuenta bancaria de la tienda.
        :param capacidadMaximaMaterial: Capacidad máxima para materiales.
        :param capacidadMaximaConsumible: Capacidad máxima para consumibles.
        :param capacidadMaximaLimpieza: Capacidad máxima para productos de limpieza.
        """
        self._nombre = nombre
        self._vendedor = vendedor
        self._cuentaBancaria = cuentaBancaria
        self._capacidadMaximaMaterial = capacidadMaximaMaterial
        self._capacidadMaximaConsumible = capacidadMaximaConsumible
        self._capacidadMaximaLimpieza = capacidadMaximaLimpieza

        # Incrementar el contador de tiendas
        Tienda.numTiendas += 1

        # Inicializar listas de productos y categorías
        self._listaProducto = []
        self._productosPorCategoria = []
        self._categorias = []
        self._conteoCategorias = []
        self.agregar()

        # Agregar la tienda a la lista de la fábrica
    def agregar(self):  
        from .Fabrica import Fabrica   
        Fabrica.getListaTienda().append(self)
        
    # Getters
    def getNombre(self):
        return self._nombre

    def getVendedor(self):
        return self._vendedor

    def getCuentaBancaria(self):
        return self._cuentaBancaria

    def getListaProducto(self):
        return self._listaProducto

    def getProductosPorCategoria(self):
        return self._productosPorCategoria

    def getCategorias(self):
        return self._categorias

    def getConteoCategorias(self):
        return self._conteoCategorias

    # Setters
    def setNombre(self, nuevoNombre):
        if isinstance(nuevoNombre, str):
            self._nombre = nuevoNombre
        else:
            raise ValueError("El nombre debe ser una cadena")

    def setVendedor(self, nuevoVendedor):
        self._vendedor = nuevoVendedor

    def setCuentaBancaria(self, nuevaCuenta):
        if isinstance(nuevaCuenta, str):
            self._cuentaBancaria = nuevaCuenta
        else:
            raise ValueError("La cuenta bancaria debe ser una cadena")

    def setListaProducto(self, nuevaLista):
        if isinstance(nuevaLista, list):
            self._listaProducto = nuevaLista
        else:
            raise ValueError("La lista de productos debe ser una lista")

    def setProductosPorCategoria(self, nuevaLista):
        if isinstance(nuevaLista, list):
            self._productosPorCategoria = nuevaLista
        else:
            raise ValueError("La lista de productos por categoría debe ser una lista")

    def setCategorias(self, nuevaLista):
        if isinstance(nuevaLista, list):
            self._categorias = nuevaLista
        else:
            raise ValueError("La lista de categorías debe ser una lista")

    def setConteoCategorias(self, nuevaLista):
        if isinstance(nuevaLista, list):
            self._conteoCategorias = nuevaLista
        else:
            raise ValueError("La lista de conteo de categorías debe ser una lista")
    



    def devolverProducto(self, factura, producto):
        from gestorAplicacion.produccion.Producto import Producto
        producto: Producto = producto
        from gestorAplicacion.gestion.Factura import Factura
        factura: Factura = factura
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que se encarga de procesar la devolución de un producto.
        """
        self._listaProducto.append(producto)
        producto.setDevuelto(True)
        return factura.getCliente() 

    
    def mostrarProductos(self, producto):
        """
        Sobreescribe el método por defecto de la clase abstracta IMostrarProducto
        Método que muestra la lista de productos omitiendo el producto dado.
        """
        return [p for p in self._listaProducto if p.getId() != producto.getId()]
    
    from typing import List
    # Método de la funcionalidad enviarPedidos:
    # Crea una lista con los productos disponibles en la tienda y la cantidad de cada uno.
    # Si un producto ya existe en la lista, incrementa su contador; de lo contrario, lo agrega como un nuevo elemento.
    def listaProductosTienda(self):
        from gestorAplicacion.produccion.Producto import Producto  # Importar Fabrica al inicio
        listaProductos = []
        
        for producto in self._listaProducto:
            encontrado = False
            if not listaProductos:
                listaProductos.append([producto, 1])
            else:
                for listaAux in listaProductos:
                    if listaAux[0].getNombre( )== producto.getNombre():
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
            texto.append(f"{i}. Producto: {producto.getNombre()}")
            texto.append(f" - Precio: {producto.getPrecio()}")
            texto.append(f" - Cantidad: {cantidad}")
            texto.append(f" - Peso: {producto.getPeso()}\n")

        return "\n".join(texto).strip()

    # Método de la funcionalidad enviarPedidos:
    # Elimina de la tienda los productos cuyos nombres coincidan con los de la lista recibida.
    def eliminarProductosPorNombre(self, listaEliminar):
        self._listaProducto = [producto for producto in self._listaProducto if producto.getNombre() not in {p.getNombre() for p in listaEliminar}]
        
    # Método de la funcionalidad enviarPedidos:
    # Genera una factura con los productos seleccionados para el pedido, junto con el cliente, el transporte y el precio de envío.
    # Devuelve la factura en formato de texto.
    def enviarPedido(self, listaProductosPedidos, transporteSeleccionado, clienteSeleccionado, precioEnvio, dia):
        from gestorAplicacion.gestion.Factura import Factura
        factura = Factura(self, clienteSeleccionado, transporteSeleccionado, listaProductosPedidos, precioEnvio, dia)
        return str(factura)

    def agregarProductosParaCambio(self, precio_cambio: float, seleccion_productos: List[int], productos_disponibles):
            from gestorAplicacion.produccion.Producto import Producto
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
                subtotal += producto_seleccionado.getPrecio()

                # Verificar si el subtotal supera el precio permitido
                if subtotal > precio_cambio:
                    break

            return productos_seleccionados

        
    def productosPorCategoria(self, productos, conteoTemporal=None):
            """
            Muestra los productos por categoría en formato: (cantidad actual/capacidad máxima).
            Si conteoTemporal se proporciona, se usa en lugar del conteo normal.
            """
            # Limpiar listas antes de procesar
            self._categorias = []

            # Lista de todas las categorías posibles
            todasLasCategorias = ["Herramientas", "Muebles", "Aseo"]
            
            # Inicializar las categorías
            for categoria in todasLasCategorias:
                self._categorias.append(categoria)
            
            # Si conteoTemporal no se proporciona, inicializar conteoCategorias
            if conteoTemporal is None:
                self._conteoCategorias = []
                self._conteoCategorias = [0] * len(self._categorias)

                # Contar productos por categoría
                for producto in productos:
                    categoria = producto.getCategoria()  # Obtener la categoría
                    if categoria in self._categorias:
                        index = self._categorias.index(categoria)
                        self._conteoCategorias[index] += 1
            else:
                # Si conteoTemporal existe, solo asegurarse de que las categorías están en la lista
                for producto in productos:
                    categoria = producto.getCategoria()
                    if categoria not in self._categorias:
                        self._categorias.append(categoria)

            # Construir el resultado
            resultado = ""
            for i, categoria in enumerate(self._categorias):
                conteo = self._conteoCategorias[i] if conteoTemporal is None else conteoTemporal[i-1]
                resultado += f"{categoria}: {conteo}/"

                # Agregar la capacidad máxima correspondiente
                if categoria == "Herramientas":
                    resultado += str(self._capacidadMaximaMaterial)
                elif categoria == "Muebles":
                    resultado += str(self._capacidadMaximaConsumible)
                elif categoria == "Aseo":
                    resultado += str(self._capacidadMaximaLimpieza)
                else:
                    resultado += "N/A"

                resultado += " productos\n"
            return resultado
    #falla aqui la actualizacion de productos por categoria
    def getCantidadActualPorCategoria(self, categoria):
            cantidad = sum(1 for producto in self._listaProducto if producto.getCategoria() == categoria)
            return cantidad
    def cantidadProductos(self):
            """
            Muestra los productos de la tienda de forma ordenada (producto: cantidad).
            """
            nombresContados = []
            resultado = ""

            for producto in self._listaProducto:
                if producto.getNombre() not in nombresContados:
                    cantidad = sum(1 for p in self._listaProducto if p.getNombre() == producto.getNombre())
                    nombresContados.append(producto.getNombre())
                    resultado += f"{producto.getNombre()}: {cantidad} unidades\n"

            return resultado

    def descargarProducto(self, transporteSeleccionado):
            """
            Descarga los productos transportados a la tienda y vacía la lista del transporte.
            """
            productosTransportados = transporteSeleccionado.getListaDeProductos()
            self._listaProducto.extend(productosTransportados)
            transporteSeleccionado.getListaDeProductos().clear()  # Vaciar la lista de productos del transporte
    def agregarProducto(self, producto):
            """Agrega el producto a la lista sin preocuparse por duplicados"""
            self._listaProducto.append(producto)


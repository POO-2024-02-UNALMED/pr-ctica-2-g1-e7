from gestion import Cliente, Factura
from . import EstadoProducto
from .Producto import Producto
from gestion import IMostrarProductos
from typing import List
class Tienda(IMostrarProductos):
    numTiendas = 0

    def __init__(self, nombre=None, vendedor=None, cuentaBancaria=None,
                 capacidadMaximaMaterial=None, capacidadMaximaConsumible=None,
                 capacidadMaximaLimpieza=None):
        if (nombre is not None and vendedor is not None and cuentaBancaria is not None and 
            capacidadMaximaMaterial is not None and capacidadMaximaConsumible is not None and 
            capacidadMaximaLimpieza is not None):
            self.nombre = nombre
            self.vendedor = vendedor
            # Se asigna la tienda al vendedor (se asume que vendedor posee el método setTienda)
            self.vendedor.setTienda(self)
            self.cuentaBancaria = cuentaBancaria
            Tienda.numTiendas += 1
            self.listaProducto = []  # Cada tienda tiene su propia lista de productos
            self.productosPorCategoria = []  # Lista de [Producto, Categoria]
            self.categorias = []
            self.conteoCategorias = []  # Conteo de productos por categoría
            self.capacidadMaximaMaterial = capacidadMaximaMaterial
            self.capacidadMaximaConsumible = capacidadMaximaConsumible
            self.capacidadMaximaLimpieza = capacidadMaximaLimpieza
        else:
            # Constructor vacío
            pass

    def devolverProducto(self, factura: Factura, producto: Producto) -> 'Cliente':
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que se encarga de procesar la devolución de un producto.
        """
        self.listaProducto.append(producto)
        producto.estado = EstadoProducto.DEVUELTO
        return factura.cliente 

    
    def mostrarProductos(self, producto: Producto) -> List[Producto]:
        """
        Sobreescribe el método por defecto de la clase abstracta IMostrarProducto
        Método que muestra la lista de productos omitiendo el producto dado.
        """
        return [p for p in self.listaProducto if p.producto_id != producto.producto_id]
    def productosPorCategoria(self, productos, conteoTemporal=None):
        """
        Muestra los productos por categoría en formato: (cantidad actual/capacidad máxima).
        Si `conteoTemporal` se proporciona, se usa en lugar del conteo normal.
        """
        # Limpiar listas antes de procesar
        self.categorias.clear()

        # Lista de todas las categorías posibles
        todasLasCategorias = ["Herramientas", "Muebles", "Aseo"]
        
        # Inicializar las categorías
        for categoria in todasLasCategorias:
            self.categorias.append(categoria)
        
        # Si `conteoTemporal` no se proporciona, inicializar `conteoCategorias`
        if conteoTemporal is None:
            self.conteoCategorias.clear()
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
        

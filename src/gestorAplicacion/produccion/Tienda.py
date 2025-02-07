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
    

from abc import ABC
from typing import List, Optional
from produccion.Producto import Producto
from .Factura import Factura
from produccion.EstadoProducto import EstadosProducto

class IMostrarProductos(ABC):
    def mostrarProductos(self, productoOmitir):
        """
        Método que puede ser sobrescrito por las clases hijas si es necesario.
        """
        return "Este método debe ser implementado si es necesario."

    @staticmethod
    def mostrarProductosFactura(factura: 'Factura') -> str:
        if not factura or not factura.listaProductos:
            return "La factura no tiene productos."
        
        texto = [
            f"{i + 1}. {p.nombre} (devuelto)" if p.estado == EstadosProducto.DEVUELTO else f"{i + 1}. {p.nombre}"
            for i, p in enumerate(factura.listaProductos)
        ]
        
        return "\n".join(texto)

    @staticmethod
    def mostrarProductosLista(listaProductos: List['Producto']) -> str:
        if not listaProductos:
            return "No hay productos registrados o disponibles."
        
        productos = [
            f"{i + 1}. {p.nombre} - {p.peso}kg - ${p.precio} - {p.categoria}"
            for i, p in enumerate(listaProductos)
        ]
        
        return "\n".join(productos)



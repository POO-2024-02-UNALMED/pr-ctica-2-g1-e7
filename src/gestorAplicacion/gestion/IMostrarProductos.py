from abc import ABC
from typing import List, Optional
from Factura import Factura

class IMostrarProductos(ABC):
    def mostrarProductos(self, productoOmitir):
        """
        Método que puede ser sobrescrito por las clases hijas si es necesario.
        """
        return "Este método debe ser implementado si es necesario."

    @staticmethod
    def mostrarProductosFactura(factura: 'Factura') -> str:
        from produccion.EstadoProducto import EstadosProducto
        if not factura or not factura.listaProductos:
            return "La factura no tiene productos."
        
        texto = [
            f"{i + 1}. {p.nombre} (devuelto)" if p.estado == EstadosProducto.DEVUELTO else f"{i + 1}. {p.nombre}"
            for i, p in enumerate(factura.listaProductos)
        ]
        
        return "\n".join(texto)

    @staticmethod
    def mostrarProductosLista(listaProductos) -> str:
        from produccion.Producto import Producto
        listaProductos: list[Producto] = listaProductos
        if not listaProductos:
            return "No hay productos registrados o disponibles."
        
        productos = [
            f"{i + 1}. {p.nombre} - {p.peso}kg - ${p.precio} - {p.categoria}"
            for i, p in enumerate(listaProductos)
        ]
        
        return "\n".join(productos)



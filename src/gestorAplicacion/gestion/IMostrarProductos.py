from abc import ABC
from typing import List, Optional

class IMostrarProductos(ABC):
    def mostrarProductos(self, productoOmitir):
        """
        Método que puede ser sobrescrito por las clases hijas si es necesario.
        """
        return "Este método debe ser implementado si es necesario."

    def mostrarProductosFactura(self) -> str:
        texto = [
            f"{i + 1}. {p.getNombre()} (devuelto)" if p.getDevuelto() else f"{i + 1}. {p.getNombre()}"
            for i, p in enumerate(self.getListaProductos())
        ]
        
        return "\n".join(texto)

    @staticmethod
    def mostrarProductosLista(listaProductos) -> str:
        from gestorAplicacion.produccion.Producto import Producto
        listaProductos: list[Producto] = listaProductos
        if not listaProductos:
            return "No hay productos registrados o disponibles."
        
        productos = [
            f"{i + 1}. {p.nombre} - {p.peso}kg - ${p.precio} - {p.categoria}"
            for i, p in enumerate(listaProductos)
        ]
        
        return "\n".join(productos)



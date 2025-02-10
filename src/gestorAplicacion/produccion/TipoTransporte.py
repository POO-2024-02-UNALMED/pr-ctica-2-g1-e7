from enum import Enum
from typing import List
import sys

class TipoTransporte(Enum):
    CAMION = (15000, 16329, "Camion")
    AVION = (30000, 64000, "Avion")
    AUTOMOVIL = (9000, 500, "Automovil")
    CAMIONETA = (12000, 650, "Camioneta")
    BICICLETA = (5000, 35, "Bicicleta")
    PATINES = (3000, 20, "Patines")
    BARCO = (20000, 3356835, "Barco")
    HELICOPTERO = (70000, 29000, "Helicoptero")
    TREN = (20000, 30000, "Tren")
    CAMINANDO = (5000, 15, "Caminando")
   
    def __init__(self, precioEnvio, capacidadMax, nombre):
        self.precioEnvio = precioEnvio
        self.capacidadMax = capacidadMax
        self.nombre = nombre
    
    """Bosquejo"""

    @classmethod
    def crear_tipo_transporte_segun_carga(cls, peso_total_productos: float) -> List['TipoTransporte']:
        """ Crear lista según la carga."""
        lista_filtrada = []
        for transporte in cls:
            if peso_total_productos <= transporte.capacidadMax:
                lista_filtrada.append(transporte)
        return lista_filtrada
    "Jose luis no hay sorecarga en python...entonces falta un metodo"
    @classmethod
    def mostrar_tipo_transporte_segun_carga(cls, lista_filtrada: List['TipoTransporte'], envio_gratis_recomendado: bool = False) -> str:
        """Display filtered transport options as a formatted string."""
        if not lista_filtrada:
            return "No hay tipos de transporte disponibles para esta carga."

        # Encuentra el transporte recomendado
        precio_minimo = sys.float_info.max
        transporte_recomendado = None
        for transporte in lista_filtrada:
            if transporte.precioEnvio < precio_minimo:
                precio_minimo = transporte.precioEnvio
                transporte_recomendado = transporte

        # Construir string para mostrar los transportes disponibles
        resultado = ""
        for i, transporte in enumerate(lista_filtrada, 1):
            precio = 0 if (transporte == transporte_recomendado and envio_gratis_recomendado) else transporte.precioEnvio
            resultado += f"{i}. {transporte.nombre} (Precio: {precio}, Capacidad Máxima: {transporte.capacidadMax}"
            
            if transporte == transporte_recomendado:
                resultado += " ---- TRANSPORTE RECOMENDADO"
            
            resultado += ")\n"

        return resultado
    """Respectiva mejora(Yhan): Selecciona un transporte de la lista filtrada según el número de opción.
       Si la opción no es válida, devuelve el transporte recomendado."""
    @staticmethod
    def seleccionar_transporte(lista_filtrada: List['TipoTransporte'], opcion: int) -> 'TipoTransporte':
        try:
            if 0 < opcion <= len(lista_filtrada):
                return lista_filtrada[opcion - 1]
            else:
                _, transporte_recomendado = TipoTransporte.mostrar_tipo_transporte_segun_carga(lista_filtrada)
                if transporte_recomendado:
                    print(f"Opción inválida. Se seleccionará automáticamente el transporte recomendado: {transporte_recomendado.nombre}")
                    return transporte_recomendado
                else:
                    raise ValueError("No hay transportes disponibles.")
        except ValueError as e:
            print(f"Error: {e}")
            return None

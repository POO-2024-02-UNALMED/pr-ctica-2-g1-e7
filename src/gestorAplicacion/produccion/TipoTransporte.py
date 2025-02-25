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
        self.__precioEnvio = precioEnvio
        self.__capacidadMax = capacidadMax
        self.__nombre = nombre
    
    """Bosquejo"""

    @classmethod
    def crearTipoTransporteSegunCarga(cls, pesoTotalProductos: float) -> List['TipoTransporte']:
        """ Crear lista según la carga."""
        listaFiltrada = []
        for transporte in cls:
            if pesoTotalProductos <= transporte.__capacidadMax:
                listaFiltrada.append(transporte)
        return listaFiltrada
    "Jose luis no hay sorecarga en python...entonces falta un metodo"
    @classmethod
    def mostrarTipoTransporteSegunCarga(cls, listaFiltrada: List['TipoTransporte'], envioGratisRecomendado: bool = False) -> str:
        """Display filtered transport options as a formatted string."""
        if not listaFiltrada:
            return "No hay tipos de transporte disponibles para esta carga."

        # Encuentra el transporte recomendado
        precioMinimo = sys.float_info.max
        transporteRecomendado = None
        for transporte in listaFiltrada:
            if transporte.__precioEnvio < precioMinimo:
                precioMinimo = transporte.__precioEnvio
                transporteRecomendado = transporte

        # Construir string para mostrar los transportes disponibles
        resultado = ""
        for i, transporte in enumerate(listaFiltrada, 1):
            precio = 0 if (transporte == transporteRecomendado and envioGratisRecomendado) else transporte.__precioEnvio
            resultado += f"{i}. {transporte.__nombre} (Precio: {precio}, Capacidad Máxima: {transporte.__capacidadMax}"
            
            if transporte == transporteRecomendado:
                resultado += " ---- TRANSPORTE RECOMENDADO"
            
            resultado += ")\n"

        return resultado
    """Respectiva mejora(Yhan): Selecciona un transporte de la lista filtrada según el número de opción.
       Si la opción no es válida, devuelve el transporte recomendado."""
    @staticmethod
    def seleccionarTransporte(lista_filtrada: List['TipoTransporte'], opcion: int) -> 'TipoTransporte':
        try:
            if 0 < opcion <= len(lista_filtrada):
                return lista_filtrada[opcion - 1]
            else:
                _, transporte_recomendado = TipoTransporte.mostrarTipoTransporteSegunCarga(lista_filtrada)
                if transporte_recomendado:
                    print(f"Opción inválida. Se seleccionará automáticamente el transporte recomendado: {transporte_recomendado.getNombre()}")
                    return transporte_recomendado
                else:
                    raise ValueError("No hay transportes disponibles.")
        except ValueError as e:
            print(f"Error: {e}")
            return None
        
    #getters y setters
    def getPrecioEnvio(self):
        return self.__precioEnvio

    def setPrecioEnvio(self, precioEnvio):
        self.__precioEnvio = precioEnvio

    def getCapacidadMax(self):
        return self.__capacidadMax

    def setCapacidadMax(self, capacidadMax):
        self.__capacidadMax = capacidadMax

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

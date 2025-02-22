from .FormatoFechaErrado import FormatoFechaErrado

class FechaFueraDeRango(Exception):
    def __init__(self, mensaje1, mensaje2):
        self.mensaje = f"La fecha es {mensaje1} a la fecha {mensaje2}"
        super().__init__(self.mensaje)
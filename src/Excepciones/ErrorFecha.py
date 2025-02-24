from .ErrorAplicacion import ErrorAplicacion

class FormatoFechaErrado(ErrorAplicacion):
    def __init__(self, mensaje):
        self.mensaje = f"Error de fecha: {mensaje}"
        super().__init__(mensaje)

class FechaFueraDeRango(FormatoFechaErrado):
    def __init__(self, mensaje1, mensaje2):
        self.mensaje = f"\nLa fecha es {mensaje1} a la fecha {mensaje2}"
        super().__init__(self.mensaje)

class PatronFechaIncorrecto(FormatoFechaErrado):
    def __init__(self, valor):
        self.valor = valor
        super().__init__(f"\nEl patrón de fecha '{valor}' no es correcto")

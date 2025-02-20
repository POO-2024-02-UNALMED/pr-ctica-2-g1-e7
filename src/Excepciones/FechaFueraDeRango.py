from FormatoFechaErrado import FormatoFechaErrado

class FechaFueraDeRango(FormatoFechaErrado):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
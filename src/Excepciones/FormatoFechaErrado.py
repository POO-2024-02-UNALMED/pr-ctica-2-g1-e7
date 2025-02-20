from ErrorAplicacion import ErrorAplicacion

class FormatoFechaErrado(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__(mensaje)
"""Error general de la aplicación"""
class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
"""Error general de la aplicación"""
class ErrorAplicacion(Exception):

    def __init__(self, mensaje):
        self.mensaje_error_inicial = "Manejo de errores de la aplicacion:"+ mensaje
        super().__init__(self.mensaje_error_inicial)
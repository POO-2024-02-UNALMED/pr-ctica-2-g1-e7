from src.Excepciones import ErrorAplicacion

class EnteroFueraDeRango(ErrorAplicacion):
    def __init__(self, mensaje):
        self.mensaje_fallo_num = f'Fallo numérico: {mensaje}'
        super().__init__(self.mensaje_fallo_num)

    def __str__(self):
        return self.mensaje
    
class CantidadFueraDeRango(EnteroFueraDeRango):
    def __init__(self, num):
        self.mensaje_error = f'\nEl número {num} está fuera de las cantidades establecidas'
        super().__init__(self.mensaje_error)

class OpcionNoValida:
    def __init__(self, num):
        self.mensaje_error = f'La opción {num} no es válida'
        super().__init__(self.mensaje_error)
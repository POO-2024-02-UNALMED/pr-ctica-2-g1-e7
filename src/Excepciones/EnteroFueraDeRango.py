from Excepciones.ErrorAplicacion import ErrorAplicacion

class EnteroFueraDeRango(ErrorAplicacion):
    def __init__(self, mensaje):
        self.mensaje_fallo_num = "Fallo numérico: " + mensaje
        super().__init__(self.mensaje_fallo_num)
    
class CantidadFueraDeRango(EnteroFueraDeRango):
    def __init__(self, num):
        self.mensaje_error = f"\nEl número {num} está fuera de las cantidades establecidas"
        super().__init__(self.mensaje_error)

class OpcionNoValida(EnteroFueraDeRango):
    def __init__(self, num):
        self.mensaje_error = f"La opción {num} no es válida"
        super().__init__(self.mensaje_error)
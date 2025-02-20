from FormatoFechaErrado import FormatoFechaErrado

class PatronFechaIncorrecto(FormatoFechaErrado):
    def __init__(self, valor):
        self.valor = valor
        super().__init__(f"El patrón de fecha '{valor}' no es correcto")
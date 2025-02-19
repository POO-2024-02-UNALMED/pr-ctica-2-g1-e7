class Meta:
    def __init__(self, nivel_de_dificultad: str, indice: float, pago: float):
        self.nivelDeDificultad = nivel_de_dificultad
        self.indice = indice
        self.pago = pago
        self.verificador = False
    
    def cumpleMeta(self, indice_de_trabajo: float) -> bool:
        return self.indice <= indice_de_trabajo
    
    def porcentajeCumplidos(self, indice_de_trabajo: float) -> str:
        porcentajeIndice = round((indice_de_trabajo * 100) / self.indice, 2)
        mensaje = f"Porcentaje de la meta logrado: {porcentajeIndice}%"
        
        if porcentajeIndice < 100:
            porcentajeFaltante = round(100 - porcentajeIndice, 2)
            mensaje += f"\nPorcentaje faltante: {porcentajeFaltante}%"
            mensaje += f"\nCantidad faltante del índice indicado: {self.indice - indice_de_trabajo}"
        
        return mensaje
    
    def __str__(self) -> str:
        return (f"\nNivel de dificultad: {self.nivelDeDificultad}\n"
                f"Índice requerido para cumplir la meta: {self.indice}\n"
                f"Recompensa por meta lograda: {self.pago}")
    
    # Getters y Setters
    def getVerificador(self) -> bool:
        return self.verificador
    
    def setVerificador(self, valor: bool):
        self.verificador = valor
    
    def getNivelDeDificultad(self) -> str:
        return self.nivelDeDificultad
    
    def setNivelDeDificultad(self, nivel_de_dificultad: str):
        self.nivelDeDificultad = nivel_de_dificultad
    
    def getIndice(self) -> float:
        return self.indice
    
    def setIndice(self, indice: float):
        self.indice = indice
    
    def getPago(self) -> float:
        return self.pago
    
    def setPago(self, pago: float):
        self.pago = pago

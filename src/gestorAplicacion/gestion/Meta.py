class Meta:
    def __init__(self, nivel_de_dificultad: str, indice: float, pago: float):
        self._nivelDeDificultad = nivel_de_dificultad
        self._indice = indice
        self._pago = pago
        self._rificador = False
    
    def cumpleMeta(self, indice_de_trabajo: float) -> bool:
        return self._indice <= indice_de_trabajo
    
    def porcentajeCumplidos(self, indice_de_trabajo: float) -> str:
        porcentajeIndice = round((indice_de_trabajo * 100) / self._indice, 2)
        mensaje = f"Porcentaje de la meta logrado: {porcentajeIndice}%"
        
        if porcentajeIndice < 100:
            porcentajeFaltante = round(100 - porcentajeIndice, 2)
            mensaje += f"\nPorcentaje faltante: {porcentajeFaltante}%"
            mensaje += f"\nCantidad faltante del índice indicado: {self._indice - indice_de_trabajo}"
        
        return mensaje
    
    def __str__(self) -> str:
        return (f"\nNivel de dificultad: {self._nivelDeDificultad}\n"
                f"Índice requerido para cumplir la meta: {self._indice}\n"
                f"Recompensa por meta lograda: {self._pago}")
    
    # Getters y Setters
    def getVerificador(self) -> bool:
        return self._verificador
    
    def setVerificador(self, valor: bool):
        self._verificador = valor
    
    def getNivelDeDificultad(self) -> str:
        return self._nivelDeDificultad
    
    def setNivelDeDificultad(self, nivel_de_dificultad: str):
        self._nivelDeDificultad = nivel_de_dificultad
    
    def getIndice(self) -> float:
        return self._indice
    
    def setIndice(self, indice: float):
        self._indice = indice
    
    def getPago(self) -> float:
        return self._pago
    
    def setPago(self, pago: float):
        self._pago = pago

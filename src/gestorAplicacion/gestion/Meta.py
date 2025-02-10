class Meta:
    def __init__(self, nivel_de_dificultad: str, indice: float, pago: float):
        self.nivel_de_dificultad = nivel_de_dificultad
        self.indice = indice
        self.pago = pago
        self.verificador = False
    
    def cumple_meta(self, indice_de_trabajo: float) -> bool:
        return self.indice <= indice_de_trabajo
    
    def porcentaje_cumplidos(self, indice_de_trabajo: float) -> str:
        porcentaje_indice = round((indice_de_trabajo * 100) / self.indice, 2)
        mensaje = f"Porcentaje de la meta logrado: {porcentaje_indice}%"
        
        if porcentaje_indice < 100:
            porcentaje_faltante = round(100 - porcentaje_indice, 2)
            mensaje += f"\nPorcentaje faltante: {porcentaje_faltante}%"
            mensaje += f"\nCantidad faltante del índice indicado: {self.indice - indice_de_trabajo}"
        
        return mensaje
    
    def __str__(self) -> str:
        return (f"\nNivel de dificultad: {self.nivel_de_dificultad}\n"
                f"Índice requerido para cumplir la meta: {self.indice}\n"
                f"Recompensa por meta lograda: {self.pago}")
    
    # Getters y Setters
    def get_verificador(self) -> bool:
        return self.verificador
    
    def set_verificador(self, valor: bool):
        self.verificador = valor
    
    def get_nivel_de_dificultad(self) -> str:
        return self.nivel_de_dificultad
    
    def set_nivel_de_dificultad(self, nivel_de_dificultad: str):
        self.nivel_de_dificultad = nivel_de_dificultad
    
    def get_indice(self) -> float:
        return self.indice
    
    def set_indice(self, indice: float):
        self.indice = indice
    
    def get_pago(self) -> float:
        return self.pago
    
    def set_pago(self, pago: float):
        self.pago = pago
